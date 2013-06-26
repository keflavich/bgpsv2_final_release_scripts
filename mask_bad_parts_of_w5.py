import pyfits
import numpy as np

w5file = './{0}/v2.0_ds2_w5_13pca_{0}map20.fits'

for filetype in '','noise':
    print w5file.format(filetype)

    w5pyfits = pyfits.open(w5file.format(filetype))

    w5pyfits[0].data[:1095,17:543] = np.nan
    w5pyfits[0].data[:525,1626:2601] = np.nan

    w5pyfits.writeto('./{0}/v2.0_ds2_w5_13pca_{0}map20_cleaned.fits'.format(filetype),
            clobber=True)
