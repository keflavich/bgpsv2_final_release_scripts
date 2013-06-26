########################################################
# Started Logging At: 2012-09-06 10:26:32
########################################################

########################################################
# # Started Logging At: 2012-09-06 10:26:33
########################################################
import matplotlib
import numpy
import numpy as np
errstate = np.seterr(all="ignore")
import agpy
T = agpy.readcol('/Volumes/disk2/data/bgps/releases/v2.0/final/bolocat/bgps_v2.0_culled_ipac.txt',asStruct=True)
print T.glon_max[T.field=='gemob1']
T.field
print T.glon_max[T.field=='gemob1b']
print (T.glon_max[T.field=='gemob1b']-188)*3600
print (T.glon_max[T.field=='gemob1b']-188)*3600/7.2
print (T.glon_max[T.field=='gemob1b']-189)*3600/7.2
print (T.glon_max[T.field=='w5']-136)*3600/7.2
print (T.glon_max[T.field=='sh235']-136)*3600/7.2
print (T.glon_max[T.field=='sh235'])*3600/7.2 % 1
print ((T.glon_max[T.field=='sh235'])*3600/7.2 % 1)*10
print ((T.glon_max[T.field=='orionB'])*3600/7.2 % 1)*10
