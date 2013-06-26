import aplpy
from pylab import *
import glob
import os

print aplpy.__version__

filelist=glob.glob('v2*fits')
filelist=glob.glob('v2*_map20.fits')
#filelist=glob.glob('v2*_crop.fits')
filelist += glob.glob('v2*_medmap20.fits')

for file in filelist:
    print file
    cropfile = file.replace("_map20","_map20_crop")
    if os.path.exists(cropfile):
        file = cropfile
    try:
        F = aplpy.FITSFigure(file,figure=figure(1),convention='calabretta')
    except TypeError:
        continue

    if "med" in file:
        repstr = "_medmap20.fits"
    else:
        repstr = "_map20.fits"

    print "The initialization succeeded"
    F.set_tick_labels_xformat("ddd.dd")
    F.set_tick_labels_yformat("dd.dd")
    F.show_grayscale()
    F.save("quicklook/"+file.replace("fits","png"))
    regfilename = "bolocat/"+file.replace(repstr,"_big.reg")
    if not (regfilename[-3:] == "reg"): 
        regfilename = "bolocat/"+file.replace("_map20_crop.fits","_big.reg")
    if os.path.exists(regfilename):
        F.show_regions(regfilename)
        F.save("quicklook/"+file.replace(".fits","_withbolocatreg.png"))
        F.hide_layer('region_set_1_txt')
        F.save("quicklook/"+file.replace(".fits","_withbolocatell.png"))
    maskfilename = regfilename.replace("_big.reg","_labelmask.fits")
    if os.path.exists(maskfilename):
        # change this to "if layer in F.layers" but need to find out correct syntax
        if os.path.exists(regfilename): F.hide_layer('region_set_1')
        F.show_contour(maskfilename, convention='calabretta', levels=[0.5], colors=['r'])
        F.save("quicklook/"+file.replace(".fits","_withbolocatmask.png"))
        F.remove_layer('contour_set_1')
        F.show_contour(maskfilename, convention='calabretta', levels=arange(1,201)-0.5, colors=['r']*200, linewidths=0.1)
        F.save("quicklook/"+file.replace(".fits","_withbolocatfinemask.png"))
    clf()
    close(1)
    del F
