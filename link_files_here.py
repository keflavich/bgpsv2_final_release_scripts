#!/usr/bin/python
import os
import sys

pwd='/Volumes/disk2/data/bgps/releases/v2.0/final'

OKfiles = [
        'l351',
        'l354',
        'l357',
        'l359',
        'l000',
        'l001',
        'l004',
        'l006',
        'l009',
        'l012',
        'l015',
        'l018',
        'l024', # still some streaks, but not gonna get any better
        'l028',
        'l029',
        'l030',
        'l031',
        'l032',
        'l035',
        'l036',
        'l040',
        'l045',
        'l050',
        'l055',
        'l060',
        'l065', # bad, but as good as it's gonna get
        'l072',
        'l077',
        'l079',
        'l080',
        'l081',
        'l082',
        'l086',
        'l089', 
        'l106'
        'l110.5n',
        'l110.5s',
        'l111.5n',
        'l111.5s',
        'l111n',
        'l111w',
        'l111s',
        'l119',
        'l123',
        'l126',
        'l129',
        'l154',
        'l169',
        'l181',
        'l182',
        'l195',
        'l201',
        'l217',
        'ic1396', # bad but not getting better =(
        'orionBnorth',
        'camob1',
        'gemob1a',
        'gemob1b',
        'ngc2264',
        'iras_22172',
        'sh235',
        'monr2',
        'orionAspine',
        'orionB',
        'w3',
        'w5',
        ]

for fieldname in OKfiles:
    os.system("find /Volumes/disk3/adam_work/ -name 'v2.0_ds2_%s*_13pca_map20.fits' -newermt '2011-12-31 00:00' -maxdepth 2 | xargs -I {} ln -s {} %s/" % (fieldname, pwd) )
    os.system("find /Volumes/disk3/adam_work/ -name 'v2.0_ds2_%s*_13pca_medmap20.fits' -newermt '2011-12-31 00:00' -maxdepth 2 | xargs -I {} ln -s {} %s/" % (fieldname, pwd) )
    os.system("find /Volumes/disk3/adam_work/ -name 'v2.0_ds2_%s*_13pca_madmap20.fits' -newermt '2011-12-31 00:00' -maxdepth 2 | xargs -I {} ln -s {} %s/noise/" % (fieldname, pwd) )
    os.system("find /Volumes/disk3/adam_work/ -name 'v2.0_ds2_%s*_13pca_noisemap20.fits' -newermt '2011-12-31 00:00' -maxdepth 2 | xargs -I {} ln -s {} %s/noise/" % (fieldname, pwd) )
    os.system("find /Volumes/disk3/adam_work/ -name 'v2.0_ds2_%s*_bolocat.sav' -newermt '2011-12-31 00:00' -maxdepth 2 | xargs -I {} ln -s {} %s/bolocat/" % (fieldname, pwd) )
    os.system("find /Volumes/disk3/adam_work/ -name 'v2.0_ds2_%s*.reg' -newermt '2011-12-31 00:00' -maxdepth 2 | xargs -I {} ln -s {} %s/bolocat/" % (fieldname, pwd) )
    os.system("find /Volumes/disk3/adam_work/ -name 'v2.0_ds2_%s*_labelmask.fits' -newermt '2011-12-31 00:00' -maxdepth 2 | xargs -I {} ln -s {} %s/bolocat/" % (fieldname, pwd) )

renames = {
        'camob1'      :'l141',
        'gemob1a'     :'l192',
        'gemob1b'     :'l189',
        'ic1396'      :'l099',
        'iras_22172'  :'l103',
        'monr2'       :'l214',
        'ngc2264'     :'l203',
        'orionAspine' :'l212',
        'orionB'      :'l207',
        'orionBnorth' :'l204',
        'sh235'       :'l174',
        'w3'          :'l133',
        'w5'          :'l137',
        }

for k,v in renames.iteritems():
    os.system("ln v2.0_ds2_%s_map20.fits v2.0_ds2_%s_map20.fits" % (k,v))
    os.system("ln v2.0_ds2_%s_medmap20.fits v2.0_ds2_%s_medmap20.fits" % (k,v))
    os.system("ln noise/v2.0_ds2_%s_noisemap20.fits noise/v2.0_ds2_%s_noisemap20.fits" % (k,v))
        

milkyway="ginsbura@milkyway.colorado.edu"
os.system('rsync -CavpuL --partial --progress --rsh=ssh --exclude "*EMBAR*" --exclude "*bck" --exclude "*.sh" --exclude "*.py" --exclude "*_area.fits" ./ %s:/home/milkyway/faculty/jaguirre/public_html/BGPS_v2_final/' % (milkyway))
os.system('rsync -CavpuL --partial --progress --rsh=ssh --exclude "*EMBAR*" --exclude "*bck" --exclude "*.sh" --exclude "*.py" --exclude "*_area.fits" noise/ %s:/home/milkyway/faculty/jaguirre/public_html/BGPS_v2_final/noise/' % (milkyway))
os.system('rsync -CavpuL --partial --progress --rsh=ssh --exclude "*EMBAR*" --exclude "*bck" --exclude "*.sh" --exclude "*.py" --exclude "*_area.fits" bolocat/ %s:/home/milkyway/faculty/jaguirre/public_html/BGPS_v2_final/bolocat/' % (milkyway))
os.system('rsync -CavpuL --partial --progress --rsh=ssh --exclude "*EMBAR*" --exclude "*bck" --exclude "*.sh" --exclude "*.py" --exclude "*_area.fits" quicklook/ %s:/home/milkyway/faculty/jaguirre/public_html/BGPS_v2_final/quicklook/' % (milkyway))
