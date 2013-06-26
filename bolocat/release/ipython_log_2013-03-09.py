########################################################
# Started Logging At: 2013-03-09 20:23:51
########################################################

########################################################
# # Started Logging At: 2013-03-09 20:23:51
########################################################
import matplotlib
import numpy
import numpy as np
errstate = np.seterr(all="ignore")
import glob
for fn in glob.glob("*.fits"):
    d = pyfits.getdata(fn)
    
import pyfits
for fn in glob.glob("*.fits"):
    d = pyfits.getdata(fn)
    print "%35s %20i %20i" % (fn,d.min(),d.max())
    
