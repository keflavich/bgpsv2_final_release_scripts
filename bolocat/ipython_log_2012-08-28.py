########################################################
# Started Logging At: 2012-08-28 13:36:58
########################################################

import matplotlib
import numpy
import numpy as np
errstate = np.seterr(all="ignore")
########################################################
# Started Logging At: 2012-08-28 13:37:09
########################################################

import matplotlib
import numpy
import numpy as np
errstate = np.seterr(all="ignore")
########################################################
# Started Logging At: 2012-08-28 13:37:47
########################################################

import matplotlib
import numpy
import numpy as np
errstate = np.seterr(all="ignore")
import idlsave
import atpy
import numpy
import glob
from pylab import *
import progressbar
widgets = [progressbar.FormatLabel('Processed %(value)d files in %(elapsed)s'),progressbar.Percentage()]
progress = progressbar.ProgressBar(widgets=widgets)
fl = glob.glob('/Volumes/disk3/adam_work/*/*_bolocat.sav')
fn = fl.pop(0)
B = idlsave.read(fn).bolocat_struct
B
B
for fn in progress(fl):
        B = numpy.hstack((B,idlsave.read(fn).bolocat_struct))
    
B
len(B)
fn
x=idlsave.read(fn).bolocat_struct
print x
numpy.hstack([B,x])
get_ipython().magic(u"pdb")
numpy.hstack([B,x])
########################################################
# Started Logging At: 2012-08-28 13:41:14
########################################################

import matplotlib
import numpy
import numpy as np
errstate = np.seterr(all="ignore")
get_ipython().magic(u"paste")
B.dtype.names
data = dict([(n,B[n]) for n in B.dtype.names])
data
get_ipython().magic(u"run ~/work/bgps_pipeline/scripts/bolocat/merge_bolocats_v2.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/scripts/bolocat/merge_bolocats_v2.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/scripts/bolocat/merge_bolocats_v2.py")
K
data[K]
B
B.filename
k
FILENAME in B
'FILENAME' in B
'filename' in B
'filename' in B.dtype.name
'filename' in B.dtype.names
'FILENAME' in B.dtype.names
get_ipython().magic(u"run ~/work/bgps_pipeline/scripts/bolocat/merge_bolocats_v2.py")
get_ipython().magic(u"history ")
