from astropy import units as u
import pandas as pd
import matplotlib.pyplot as plt
import pickle

with open('data/h_alpha.pickle', 'rb') as f:
    dc_wave, dc_flux, dc_model = pickle.load(f)
    
df = pd.read_csv('data/h_alpha.csv')

i = 3

lam_rest = df.loc[df['n']==i, 'lam_rest'].iloc[0]
lam_obs = df.loc[df['n']==i, 'lam_obs'].iloc[0]
z = df.loc[df['n']==i, 'z'].iloc[0]

from specutils import Spectrum1D, SpectralRegion
from specutils.fitting.continuum import fit_continuum
from specutils.analysis import equivalent_width


spectrum = Spectrum1D(spectral_axis=dc_wave[i], flux=dc_model[i])

model = fit_continuum(spectrum, window=(4000*u.AA, 9000*u.AA))
continuum = model(spectrum.spectral_axis)
flux_norm = spectrum.flux / continuum

#a = equivalent_width(spec)


fig, ax = plt.subplots(2,1)
ax[0].plot(dc_wave[i].value, spectrum.flux.value, c='b')
ax[0].plot(dc_wave[i].value, continuum.value, c='r')
ax[1].plot(dc_wave[i].value, flux_norm.value)
ax[0].axvline(x=lam_obs, c='r', ls='--', lw=0.5, alpha=0.5)
ax[1].axvline(x=lam_obs, c='r', ls='--', lw=0.5, alpha=0.5)
ax[0].axvline(x=lam_rest, c='g', ls='--', lw=0.5, alpha=0.5)
ax[1].axvline(x=lam_rest, c='g', ls='--', lw=0.5, alpha=0.5)
ax[0].grid()
ax[1].grid()
ax[0].set_xlim(6500, 6630)
ax[1].set_xlim(6500, 6630)
plt.show()

