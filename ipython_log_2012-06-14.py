########################################################
# Started Logging At: 2012-06-14 11:17:05
########################################################

import ypfits
f1 = pyfits.open('
import pyfits
f1 = pyfits.open('mosaics/MOSAIC_MAP_V2.fits')
get_ipython().system(u'find . -name "*MOSAIC*noise*"')
f2 = pyfits.open('noise/MOSAIC_v2_NOISE.fits')
f1[0].data = f1[0].data/f2[0].noise
f1[0].data = f1[0].data/f2[0].data
f1.writeto('mosaics/MOSAIC_SIGNAL_TO_NOISE_V2.fits')
