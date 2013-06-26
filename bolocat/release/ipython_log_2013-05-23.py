########################################################
# Started Logging At: 2013-05-23 14:36:20
########################################################

########################################################
# # Started Logging At: 2013-05-23 14:36:22
########################################################
import matplotlib
import numpy
import numpy as np
errstate = np.seterr(all="ignore")
table = agpy.readcol("/Volumes/disk2/data/bgps/releases/v2.0/final/bolocat/bgps_v2.0_culled_ipac.txt",asRecArray=True)
import agpy
table = agpy.readcol("/Volumes/disk2/data/bgps/releases/v2.0/final/bolocat/bgps_v2.0_culled_ipac.txt",asRecArray=True)
get_ipython().system(u'ls -F -G ')
get_ipython().magic(u'run ~/work/bgps_pipeline/bolocat/export_v2.py')
fixed_table
get_ipython().magic(u'pinfo fixed_table.rename_column')
for old,new in [('glon_max','glon_peak'),('glat_max','glat_peak'),('maxra','ra'),('maxdec','dec'),('f','flux'),('ef','err_flux')]:
        fixed_table.rename(old,new)
    
for old,new in [('glon_max','glon_peak'),('glat_max','glat_peak'),('maxra','ra'),('maxdec','dec'),('f','flux'),('ef','err_flux')]:
        fixed_table.rename_column(old,new)
    
fixed_table.write("/Volumes/disk2/data/bgps/releases/v2.0/final/bolocat/bgps_v2.0_culled_ipac_sorted.txt",type='ipac',overwrite=True)
get_ipython().magic(u'run ~/work/bgps_pipeline/bolocat/export_v2.py')
get_ipython().magic(u'paste')
for old,new in [('glon_max','glon_peak'),('glat_max','glat_peak'),('maxra','ra'),('maxdec','dec'),('f','flux'),('ef','err_flux'),
        ('f40','flux_40'),('ef40','err_flux_40'),
        ('f80','flux_80'),('ef80','err_flux_80'),
        ('f120','flux_120'),('ef120','err_flux_120'),
        ('radius','rad'),
        ('cloudn','cnum'),
        ('glon','glon_cen'),
        ('glat','glat_cen'),
        ('mommaj','maj'),
        ('mommin','min'),
        ('pa','pos_ang'),
        ]:
    fixed_table.rename_column(old,new)
fixed_table.write("/Volumes/disk2/data/bgps/releases/v2.0/final/bolocat/bgps_v2.0_culled_ipac_sorted.txt",type='ipac',overwrite=True)

get_ipython().magic(u'run ~/work/bgps_pipeline/bolocat/export_v2.py')
get_ipython().system(u'open ./')
get_ipython().magic(u'history ')
