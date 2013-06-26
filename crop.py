import pyregion
import astropy.io.fits as pyfits
import astropy.wcs as pywcs
#import pyfits
#import pywcs
import montage
import agpy
from agpy.get_cutouts import coords_in_image
import glob
import numpy as np
import os
import itertools

regfile = pyregion.open('crop_regions.reg'); temp=False
#regfile = pyregion.open('temp.reg'); temp=True

# make the headers from the regions
def reg_to_header(rectreg,cdelt=7.2/3600.):
    """
    Takes a pyregion Rectangle region and creates a header with dimensions
    equal to the box size
    """
    crval1,crval2,size1,size2,angle = rectreg.coord_list
    # convert DS9 convention to FITS convention
    if angle != 0:
        angle = -angle

    NAXIS1 = np.ceil(size1 / cdelt)
    NAXIS2 = np.ceil(size2 / cdelt)

    cdelt1 = cdelt*-1
    cdelt2 = cdelt
    cd =np.array( [[cdelt1*np.cos(angle/180.*np.pi), -np.sin(angle/180.*np.pi)*cdelt2],
          [np.sin(angle/180.*np.pi)*cdelt1, np.cos(angle/180.*np.pi)*cdelt2]] )

    header = pyfits.Header()
    header.update('BITPIX',-32)
    header.update('NAXIS',2)
    header.update('NAXIS1',int(NAXIS1))
    header.update('NAXIS2',int(NAXIS2))
    header.update('CRVAL1',crval1)
    header.update('CRVAL2',crval2)
    header.update('CRPIX1',NAXIS1/2.)
    header.update('CRPIX2',NAXIS2/2.)
    header.update('CD1_1',cd[0,0])
    header.update('CD1_2',cd[0,1])
    header.update('CD2_1',cd[1,0])
    header.update('CD2_2',cd[1,1])
    header.update('CTYPE1','GLON-CAR')
    header.update('CTYPE2','GLAT-CAR')

    return header

headerlist = [reg_to_header(reg) for reg in regfile]
regname = [reg.attr[1]['text'] for reg in regfile]
hdrdict = dict(zip(regname,headerlist))

filelist = glob.glob("v2.0_ds2*_map20.fits")
filelist += glob.glob("v2.0_ds2*_medmap20.fits")

if not temp: bounds = open('bounds.txt','w')

# for each file, find out if crval1,crval2 are in a header
for fn in filelist:
    print fn
    if "area" in fn: continue
    try:
        fits = pyfits.open(fn)
    except:
        continue
    glon = fits[0].header.get('CRVAL1')
    glat = fits[0].header.get('CRVAL2')
    for header,name in zip(headerlist,regname):
        try: 
            lname = "l%03i" % int(name)
        except:
            lname = name
        if lname in fn:
        #if coords_in_image(glon, glat, header, coordsys='galactic'):
            print header
            header.toTxtFile('temp.hdr',clobber=True)
            try:
                for ffn in (fn, "noise/"+fn.replace("_map20","_noisemap20")):
                    montage.mProject_auto(ffn,ffn.replace(".fits","_crop.fits"),'temp.hdr')
                    #montage.wrappers.mosaic(dir,'%s/mosaic' % dir,header='%s/%s' % (dir,options.header), exact_size=options.exact, combine=options.combine)
                    # do something
                    areafile = fn.replace(".fits","_crop_area.fits")
                    if "area.fits" in areafile and os.path.exists(areafile): os.remove(areafile)

                #glonx = fits[0].header.get('CRVAL1') + (fits[0].header.get('CRPIX1')+np.arange(fits[0].header.get('NAXIS1'))+1)*fits[0].header.get('CD1_1')
                wcs = pywcs.WCS(header)
                glonmin,glatmin = np.inf,np.inf
                glonmax,glatmax = -np.inf,-np.inf
                for x,y in itertools.product((1,wcs.naxis1),(1,wcs.naxis2)):
                    a,b = wcs.wcs_pix2sky(x,y,1)
                    if a < glonmin:
                        glonmin = a
                    if b < glatmin:
                        glatmin = b
                    if a > glonmax:
                        glonmax = a
                    if b > glatmax:
                        glatmax = b
                if not temp: print >>bounds,"%45s %15g %15g %15g %15g" % (fn,glonmin,glonmax,glatmin,glatmax)
                if not temp: bounds.flush()
            except montage.status.MontageError:
                pass

if not temp: bounds.close()
