########################################################
# Started Logging At: 2012-07-20 14:29:46
########################################################

########################################################
# Started Logging At: 2012-07-20 14:34:06
########################################################

########################################################
# Started Logging At: 2012-07-20 14:38:12
########################################################

########################################################
# Started Logging At: 2012-07-20 14:40:17
########################################################

########################################################
# Started Logging At: 2012-07-20 14:45:27
########################################################

get_ipython().magic(u'run ~/work/bgps_pipeline/analysis/bolocat_sizes.py')
show()
ax=gca()
get_ipython().magic(u'pinfo ax.hist')
########################################################
# Started Logging At: 2012-07-20 14:50:55
########################################################

get_ipython().magic(u'run ~/work/bgps_pipeline/analysis/bolocat_sizes.py')
show()
########################################################
# Started Logging At: 2012-07-20 15:04:57
########################################################

get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/bolocat_sizes.py")
show()
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
dfft = fftshift(fft.fft2(data.squeeze()))
draw()
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
help(hist)
help(hist)
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
help(hist)
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/bolocat_sizes.py")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
help(hist)
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
p
p.get_color()
get_ipython().magic(u"pinfo p")
get_ipython().magic(u"pinfo2 p")
list(p)
p[0]
p[0].get_color()
p
P = p[0]
P.get_ec()
P.get_fc()
P.get_alpha()
P.set_fc(array([0,0,0,0.25]))
draw()
draw()
draw()
draw()
draw()
draw()
get_ipython().magic(u"paste")
p
P = p[0]
P.get_color()
P.properties()
matplotlib.colors.ColorConverter.to_rgba('r')
matplotlib.colors.ColorConverter()
CC = matplotlib.colors.ColorConverter()
CC.to_rgba('r')
CC.to_rgba('r',0.5)
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"pinfo P")
CC.to_rgba((0,0,0,0.5))
CC.to_rgba((0,0,0,0.5),1)
CC.to_rgba((0,0,0,0.5),None)
P._fill
P._facecolor
P._edgecolor
P.draw()
P.draw(gca())
ax=gca()
get_ipython().magic(u"pinfo2 ax.add_patch")
setp 
help(setp)
setp(P)
setp(P,facecolor(0,1,0,0.25))
setp(P,facecolor=(0,1,0,0.25))
draw()
draw()
setp(P,'facecolor',(0,1,0,0.25))
draw()
P = p[0]
setp(P,'facecolor',(0,1,0,0.25))
draw()
setp(P,'facecolor',(0,1,0,0.25),zorder=2)
setp(P,'facecolor',(0,1,0,0.25),zorder=2,alpha=0.5)
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"pinfo ax.hist")
########################################################
# Started Logging At: 2012-07-20 15:54:58
########################################################

get_ipython().magic(u"paste")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/bolocat_sizes.py")
show()
get_ipython().magic(u"paste")
p2._alp
p2._alpha
p2[0]._alpha
p2[0].set_alpha(1)
draw()
p2[0].set_facecolor((0,0,1,0.1))
draw()
matplotlib.use()
help(matplotlib.use)
matplotlib.get_backend()
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/bolocat_sizes.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/bolocat_vs_longitude.py")
np.sum(     4,    15,    32,     3,    39,     5,     3,     2,     7,    13,     9,    11,    13,    10,    19,    15,    22,    64,   145,    45,    14,    65,
)
np.sum((     4,    15,    32,     3,    39,     5,     3,     2,     7,    13,     9,    11,    13,    10,    19,    15,    22,    64,   145,    45,    14,    65,))
get_ipython().magic(u"pwd ")
v2 = pyfits.getdata('noise/v2.0_ds2_l060_13pca_noisemap20.fits')
import astropy.io.fits as pyfits
v2 = pyfits.getdata('noise/v2.0_ds2_l060_13pca_noisemap20.fits')
v1 = pyfits.getdata('../../IPAC/rmsmap/v1.0.2_l065_13pca_rmsmap50.fits')
v1.shape
v2.shape
v1h = pyfits.getheader('../../IPAC/rmsmap/v1.0.2_l065_13pca_rmsmap50.fits')
v2h = pyfits.getheader('noise/v2.0_ds2_l060_13pca_noisemap20.fits')
hdr=v1h
lmin=60
lmax=61
binsize=0.5
get_ipython().magic(u"paste")
map = v1.T
get_ipython().magic(u"paste")
binsize
j=0
binsize=[0.5]
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
xu
xl
yu
yl
map
map.shape
figure()
hist(map[xl:xu,yl:yu],bins=50)
hist(map[xl:xu,yl:yu].flat,bins=50)
v1submap = map[xl:xu,yl:yu]
imshow(v1submap.T)
i
i=0
            xl = floor(least + npix * i)
            xu = floor(least + npix * (i+1))
get_ipython().magic(u"paste")
xu
xl
v1submap = map[xl:xu,yl:yu]
imshow(v1submap.T)
imshow(np.log10(v1submap.T))
v1submap
imshow(v1submap.T,vmin=0,vmax=0.1)
clf90
clf()
imshow(v1submap.T,vmin=0,vmax=0.1)
hist(v1submap.flat, bins=50)
hist(v1submap[v1submap==v1submap], bins=50)
clf()
hist(v1submap[v1submap==v1submap], bins=50)
hdr=v2h
map = v2.T
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
mapcrop
mapcrop.shape
v1submap.shape
v2submap = mapcrop
figure()
imshow(v2submap)
figure(9)
hist(v2submap[v2submap==v2submap], bins=50)
hist(1.5*v1submap[v1submap==v1submap], bins=50, alpha=0.5)
binpt5noise
least
lzero
bzero
lbin
