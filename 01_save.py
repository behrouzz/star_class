# http://skyserver.sdss.org/dr16/en/proj/basic/spectraltypes/lines.aspx

from glob import glob
from astropy.io import fits
from astropy import units as u
import pandas as pd
import matplotlib.pyplot as plt

def get_h_alpha(filename):
    n = int(filename.split('\\')[-1][0])
    hdul = fits.open(filename)

    data1 = hdul[1].data
    data3 = hdul[3].data

    wavelength = 10 ** data1.field('loglam')
    flux = data1.field('flux')
    model = data1.field('model')

    wavelength = wavelength * u.Unit('AA')
    flux = flux * 10**-17 * u.Unit('erg cm-2 s-1 AA-1')
    model = model * 10**-17 * u.Unit('erg cm-2 s-1 AA-1')

    line_names = [i for i in data3.field('LINENAME')]
    idx = line_names.index('H_alpha')
    lam_rest = [i for i in data3.field('LINEWAVE')][idx]
    z = [i for i in data3.field('LINEZ')][idx]
    area = [i for i in data3.field('LINEAREA')][idx]
    ew = [i for i in data3.field('LINEEW')][idx]
    conlev = [i for i in data3.field('LINECONTLEVEL')][idx]
    lam_obs = lam_rest * (1 + z)

    hdul.close()

    dc = {'n':n, 'wave':wavelength, 'flux':flux, 'model':model,
          'lam_rest':lam_rest, 'lam_obs':lam_obs, 'z':z,
          'area':area, 'ew':ew, 'conlev':conlev}

    return dc
    

fs = glob('stars/*.fits')
fs.sort()

ls = []
for i in fs:
    ls.append(get_h_alpha(i))

dc_wave = {}
dc_flux = {}
dc_model = {}
for i in range(len(ls)):
    n = i + 1
    dc_wave[n] = ls[i].pop('wave')
    dc_flux[n] = ls[i].pop('flux')
    dc_model[n] = ls[i].pop('model')

df = pd.DataFrame(ls)
df.set_index('n').to_csv('data/h_alpha.csv')

import pickle
with open('data/h_alpha.pickle', 'wb') as f:
    pickle.dump([dc_wave, dc_flux, dc_model], f)

    


