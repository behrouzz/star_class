# http://skyserver.sdss.org/dr16/en/proj/basic/spectraltypes/lines.aspx

from glob import glob
from astropy.io import fits

fs = glob('stars/*.fits')
fs.sort()

hdul = fits.open(fs[0])

data1 = hdul[1].data
data3 = hdul[3].data

#hdul.close()


    


