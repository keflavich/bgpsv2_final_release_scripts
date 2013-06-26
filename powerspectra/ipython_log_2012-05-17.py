########################################################
# Started Logging At: 2012-05-17 09:17:09
########################################################

fits = pyfits.open('../v2.0_ds2_gemob1a_13pca_map20.fits')
import pyfits
fits = pyfits.open('../v2.0_ds2_gemob1a_13pca_map20.fits')
import AG_fft_tools
ps = AG_fft_tools.psds.power_spectrum(fits[0].data)
ps
plot(*ps)
semilogx(*ps)
semilogx(ps[0]/7.2,ps[1])
7.2/ps[0]
7.2/ps[0]/3600.
import aplpy
aplpy.FITSFigure(fits)
aplpy.FITSFigure(fits,convention='calabretta')
FF = Out[14]
FF.show_colorscale()
f[0].data.shape
fits[0].data.shape
2055*7.2/3600.
7.2/3600/ps[0][0]
7.2/3600/ps[0][0] * 2054./2055.
7.2/3600/ps[0][0] / 4.11
((749/2.)**2+(2055/2.)**2)**0.5
((749/2.)**2+(2055/2.)**2)**0.5 * 2
((749/2.)**2+(2055/2.)**2)**0.5 * 2 / 2055.
((749/2.)**2+(2055/2.)**2)**0.5 * 2 / 2054.
((749/2.)**2+(2055/2.)**2)**0.5 * 2 
((749/2.)**2+(2055/2.)**2)**0.5 * 2 * 7.2
((749/2.)**2+(2055/2.)**2)**0.5 * 2 * 7.2/3600.
((749/2.)**2+(2055/2.)**2)**0.5 * 2 * 7.2/3600. / (7.2/3600./ps[0][0])
((749/2.)**2+(2055/2.)**2)**0.5 * 2 * 7.2/3600. / (7.2/3600./ps[0][0]) * 2055./2054.
imshow(fits[0].data)
figure()
imshow(fits[0].data)
imshow(fits[0].data[100:550,100:650])
imshow(np.log10(fits[0].data[100:550,100:650]))
imshow(np.log10(fits[0].data[175:450,250:650]))
imshow(np.log10(fits[0].data[175:500,250:700]))
clf()
imshow(np.log10(fits[0].data[175:500,250:700]))
imshow(np.log10(fits[0].data[175:450,250:650]))
clf()
imshow(np.log10(fits[0].data[175:450,250:650]))
figure(1)
ps = AG_fft_tools.psds.power_spectrum(fits[0].data[175:450,250:650])
semilogx(ps[0]/7.2,ps[1])
1/1.5e-2
1/2.5e-3
get_ipython().system(u"wcshead /Users/adam/work/bolocam/simulations/exp10/*fits")
1./xarr[16]
ps
ps[0]
xarr = np.linspace(0,0.5/7.2,ps[0].size)
semilogx(xarr,ps[1])
clf()
semilogx(xarr,ps[1])
#fill_between(xarr,ps[1]*0.9,ps[1]*1.1)
OK = (xarr>2.5e-3)*(xarr<1.5e-2)
fill_between(xarr[OK],ps[1][OK]*0.9,ps[1][OK]*1.1)
import agpy
agpy.PCA_tools.total_least_squares(np.log10(xarr[OK],ps[1][OK]))
agpy.PCA_tools.total_least_squares(np.log10(xarr[OK]),np.log10(ps[1][OK]))
agpy.PCA_tools.total_least_squares(np.log10(xarr[OK]),np.log10(ps[1][OK]),print_results=True)
OK = (xarr>4e-3)*(xarr<1.5e-2)
agpy.PCA_tools.total_least_squares(np.log10(xarr[OK]),np.log10(ps[1][OK]),print_results=True)
fill_between(xarr[OK],ps[1][OK]*0.9,ps[1][OK]*1.1,color='r',alpha=0.5)
plot(xarr[OK], 10**(np.log10(xarr[OK])*Out[65][0]+Out[65][1])
)
plot(xarr[OK], 10**(np.log10(xarr[OK])*Out[65][0]+Out[65][1], linewidth=2)
plot(xarr[OK], 10**(np.log10(xarr[OK])*Out[65][0]+Out[65][1]), linewidth=2)
0.5/7.2
0.5/7.2 / 4e-3
get_ipython().magic(u"pwd ")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
plot_connect_powerspec('/Volumes/disk2/data/bgps/releases/v2.0/final/powerspectra/v2.0_ds2_l045_13pca_map20.fits')
plot_connect_powerspec('/Volumes/disk2/data/bgps/releases/v2.0/final/powerspectra/v2.0_ds2_l045_13pca_map20.fits.fits')
plot_connect_powerspec('/Volumes/disk2/data/bgps/releases/v2.0/final/powerspectra/v2.0_ds2_l045_13pca_map20.fits')
get_ipython().magic(u"pwd ")
plot_connect_powerspec('/Volumes/disk2/data/bgps/releases/v2.0/final/powerspectra/v2.0_ds2_l045_13pca_map20.fits')
('/Volumes/disk2/data/bgps/releases/v2.0/final/powerspectra/v2.0_ds2_l045_13pca_map20.fits')[-5:]
('/Volumes/disk2/data/bgps/releases/v2.0/final/powerspectra/v2.0_ds2_l045_13pca_map20.fits')[:-5]
plot_connect_powerspec('/Volumes/disk2/data/bgps/releases/v2.0/final/powerspectra/v2.0_ds2_l045_13pca_map20.fits')
os.path.splitext('/Volumes/disk2/data/bgps/releases/v2.0/final/powerspectra/v2.0_ds2_l045_13pca_map20.fits')
os.path.splitext('/Volumes/disk2/data/bgps/releases/v2.0/final/v2.0_ds2_l045_13pca_map20.fits')
plot_connect_powerspec('/Volumes/disk2/data/bgps/releases/v2.0/final/v2.0_ds2_l045_13pca_map20.fits')
os.path.splitext('/Volumes/disk2/data/bgps/releases/v2.0/final/v2.0_ds2_l045_13pca_map20.fits')
os.path.splitext('/Volumes/disk2/data/bgps/releases/v2.0/final/powerspectra/v2.0_ds2_l045_13pca_map20.fits')
plot_connect_powerspec('/Volumes/disk2/data/bgps/releases/v2.0/final/powerspectra/v2.0_ds2_l045_13pca_map20.fits')
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
plot_connect_powerspec('/Volumes/disk2/data/bgps/releases/v2.0/final/powerspectra/v2.0_ds2_l045_13pca_map20.fits')
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
plot_connect_powerspec('/Volumes/disk2/data/bgps/releases/v2.0/final/powerspectra/v2.0_ds2_l045_13pca_map20.fits')
ion()
show()
figure()
plot_connect_powerspec('/Volumes/disk2/data/bgps/releases/v2.0/final/powerspectra/v2.0_ds2_l045_13pca_map20.fits',psdsize=128)
rr,zz = psds.power_spectrum(f[0].data)
rr,zz = psds.power_spectrum(np.ones([15,15]))
rr
rr-rr[0]
rr.shape
np.fft.fftfreq(22)
np.fft.fftfreq(22)[:11]
(rr-rr[0])/2.
import AG_image_tools
AG_image_tools.radialprofile.azimuthalAverage(np.ones([15,15]),binsize=1)
AG_image_tools.radialprofile.azimuthalAverage(np.ones([15,15]),binsize=1,azbins=[1,2,3])
AG_image_tools.radialprofile.azimuthalAverageBins(np.ones([15,15]),binsize=1,azbins=[1,2,3])
AG_image_tools.radialprofile.azimuthalAverageBins(np.ones([15,15]),binsize=1,azbins=2)
AG_image_tools.radialprofile.azimuthalAverageBins(np.ones([15,15]),binsize=1,azbins=3)
AG_image_tools.radialprofile.azimuthalAverageBins(np.ones([15,15]),binsize=1,azbins=3)[1]
AG_image_tools.radialprofile.azimuthalAverageBins(np.ones([15,15]),binsize=1,azbins=4)[1]
a,b,c = AG_image_tools.radialprofile.azimuthalAverageBins(np.ones([15,15]),binsize=1,azbins=4)
b
a,(b,c) = AG_image_tools.radialprofile.azimuthalAverageBins(np.ones([15,15]),binsize=1,azbins=4)
a,(b,c) = AG_image_tools.radialprofile.azimuthalAverageBins(np.ones([15,15]),binsize=2,azbins=4)
b
b.shape
np.linspace(0.5,10.5,11)
b.size
np.fft.fftfreq(22)[:11]
np.linspace(0.,2./11,11)
np.linspace(0.,0.5/11,11)
np.linspace(0.,5./11,11)
np.fft.fftfreq(22)
np.linspace(0.,0.5,11)
np.fft.fftfreq(22)[:11]
np.fft.fftfreq(24)[:12]
np.fft.fftfreq(24)[:13]
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
plot_connect_powerspec('/Volumes/disk2/data/bgps/releases/v2.0/final/powerspectra/v2.0_ds2_l045_13pca_map20.fits',psdsize=128)
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
plot_connect_powerspec('/Volumes/disk2/data/bgps/releases/v2.0/final/powerspectra/v2.0_ds2_l045_13pca_map20.fits',psdsize=128)
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
plot_connect_powerspec('/Volumes/disk2/data/bgps/releases/v2.0/final/powerspectra/v2.0_ds2_l045_13pca_map20.fits',psdsize=128)
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
plot_connect_powerspec('/Volumes/disk2/data/bgps/releases/v2.0/final/powerspectra/v2.0_ds2_l045_13pca_map20.fits',psdsize=128)
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
plot_connect_powerspec('/Volumes/disk2/data/bgps/releases/v2.0/final/powerspectra/v2.0_ds2_l045_13pca_map20.fits',psdsize=128)
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
plot_connect_powerspec('/Volumes/disk2/data/bgps/releases/v2.0/final/powerspectra/v2.0_ds2_l045_13pca_map20.fits',psdsize=128)
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
help(imshow)
matplotlib.cm.bone(0.0)
matplotlib.cm.bone(0.9)
matplotlib.colors.Colormap(linspace(0,1,256))
CM = matplotlib.colors.Colormap(linspace(0,1,256))
CM(0.1)
matplotlib.cm.gray(0.1)
matplotlib.cm.gray(0.9)
c = matplotlib.cm.gray
c._lut
c._lut.shape
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
figure(2)
clf()
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
help(axes)
SP = subplot(122)
SP.axes
SP.axis 
SP.get_frame()
R = SP.get_frame()
R.get_xy 
R.get_xy()
R.get_x()
R.get_y()
R.get_width90
R.get_width()
help(R.get_width)
SP.get_window_extent()
SP.get_window_extent()[0]
SP.get_window_extent().BBox
SP.get_window_extent().Bbox
TBB = SP.get_window_extent()
 SP.get_xbound()
SP.get_xbound()
SP.get_ybound()
TBB.get_points()
TBB.corners 
TBB.corners()
help(TBB.corners)
TBB.extents()
TBB.extents
TBB.bounds
TBB.x0
TBB.xmin
SP.get_window_extent()
get_ipython().magic(u"pinfo2 TBB.__repr__")
TBB._bbox
get_ipython().magic(u"pinfo2 TBB._bbox.__repr__")
TBB._bbox._points
SP._position
SP._position._points
spxmin,spxmax,spymin,spymax = SP._position._points
(spxmin,spxmax),(spymin,spymax) = SP._position._points
spxmax
number_lon
number_lon = 3
number_lat=3
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
spyxmin
spymin
spymax
[spxmin+ii*(spxmax-spxmin)/number_lon,(spxmax-spxmin)/number_lon,
                spymin+ii*(spymax-spymin)/number_lon,(spymax-spymin)/number_lon]
help(pylab.axes)
spymax
spymin
subplot(122)
plot(linspace(0,1500),rand(50))
plot(linspace(0,1500),rand(50)*1500)
SP._position._points
spymax
get_ipython().magic(u"paste")
help(pylab.axes)
get_ipython().magic(u"paste")
help(pylab.axes)
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
help(pylab.axes)
ax.plot_date()
ax.plot_date(1,2)
powerspec_grid
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"pdb")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
help(ax)
help(pylab.axes)
help(ax)
ax._position
ax._position._points
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
help(ax.set_position)
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
SP._position.get_points()
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
ax.axis 
ax.tick_params 
ax.tick_params()
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
help(imshow)
imshow(np.ones([20,100]))
figure(1)
clf()
imshow(np.ones([20,100]))
imshow(np.ones([20,100]),aspect=0.2)
imshow(np.ones([20,100]),aspect=5)
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
x = np.ones([1,5])
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
q
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
help(PCA_tools.total_least_squares)
PCA_tools.total_least_squares(arange(5),arange(5),return_error=True)
zz[newrr]
PCA_tools.total_least_squares(arange(5),arange(5),1,1return_error=True)
PCA_tools.total_least_squares(arange(5),arange(5),1,1,return_error=True)
PCA_tools.total_least_squares(arange(5),arange(5),ones(5),ones(5),return_error=True)
reload(PCA_tools)
PCA_tools.total_least_squares(arange(5),arange(5),ones(5),ones(5),return_error=True)
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
help(matplotlib.cm.jet)
help(matplotlib.cm.jet._lut)
matplotlib.cm.jet._i_bad
matplotlib.cm.jet._i_over
matplotlib.cm.jet._i_under
matplotlib.cm.jet._lut[256:,:]
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
range(1)
get_ipython().system(u"ls -F W49*png")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
get_ipython().system(u"ls -F ")
get_ipython().system(u"ls -F *crop*fits")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"paste")
get_ipython().magic(u"run ~/work/bgps_pipeline/analysis/powerspectra_per_lb.py")
""" 2.0 &         -2.9 &           17
 2.0 &         -2.5 &            5
 2.0 &         -2.5 &           14
 2.0 &         -3.3 &          256
11.2 &         -2.0 &          203
 1.6 &         -4.0 &          842
 5.3 &         -2.5 &          644
 2.1 &         -2.0 &           44
 2.1 &         -2.4 &           76
 2.1 &         -3.0 &           54
"""
T = """ 2.0 &         -2.9 &           17
 2.0 &         -2.5 &            5
 2.0 &         -2.5 &           14
 2.0 &         -3.3 &          256
11.2 &         -2.0 &          203
 1.6 &         -4.0 &          842
 5.3 &         -2.5 &          644
 2.1 &         -2.0 &           44
 2.1 &         -2.4 &           76
 2.1 &         -3.0 &           54
""".split("&")
T
tx = """ 2.0 &         -2.9 &           17
 2.0 &         -2.5 &            5
 2.0 &         -2.5 &           14
 2.0 &         -3.3 &          256
11.2 &         -2.0 &          203
 1.6 &         -4.0 &          842
 5.3 &         -2.5 &          644
 2.1 &         -2.0 &           44
 2.1 &         -2.4 &           76
 2.1 &         -3.0 &           54
"""
T = tx.split("&\n")
T
T = [t.split("\n") for t in tx.split("&")]
T
T = [float(t.split("\n")) for t in tx.split("&")]
T = [float(t.split("\n")) for t in tx.strip().split("&")]
T = [(t.split("\n")) for t in tx.strip().split("&")]
T
T = [(t.split("&")) for t in tx.strip().split("\n")]
T
T = [(t.split("&")) for t in tx.strip().split("\n")]; W = [float(t) for t in T]
T = [(t.split("&")) for t in tx.strip().split("\n")]; W = [float(t) for x in T for t in x]
W
T = [(t.split("&")) for t in tx.strip().split("\n")]; 
T
array(T)
array(T).astype('float')
T = array(T).astype('float')
T.shape
figure()
plot(T[:,0],T[:,1])
clf()
plot(T[:,0],T[:,1],'s')
subplot(221)
plot(T[:,0],T[:,1],'s')
subplot(222)
plot(T[:,2],T[:,1],'s')
subplot(223)
plot(T[:,2]*T[:,0],T[:,1],'s')
644*14*5.3**2
import pyregion
r = pyregion.read_region('../crop_regions.reg')
r = pyregion.open('../crop_regions.reg')
r
r[0]
R = r[0]
R.coord_list
get_ipython().magic(u"pwd ")
3e5/50
0.02/5.
1/(0.02/5.)
get_ipython().system(u"ls -F /var")
np.fft.fftfreq([3,3])
help(np.fft.fft2)
help(np.fft.fftfreq)
np.fft.fftfreq(5)
np.fft.fftfreq(5,7.2)
np.fft.fftfreq(5)/7.2
1/.0172512
1/0.0148912
1/0.0237014
1/0.0316742
3.5/350e-4
3.5/350e-6
350e-6/3.5 * 2026265.
350e-6/3.5 * 206265.
350e-6/3.5 * 206265. * 1.22
product([5,10])
product([4096,4096])
2**245
2**24
2**28
2**28 / 1e6
359998**2
359998**2 > 2e28
359998**2 > 2**28
help(np.linalg.svd)
np.linalg.svd(np.array([arange(1e5),arange(1e5)],full_matrices=0)
)
np.linalg.svd(np.array([arange(1e5),arange(1e5)]),full_matrices=0)
np.linalg.svd(np.array([arange(1e6),arange(1e6)]),full_matrices=0)
np.linalg.svd(np.array([arange(1e4),np.rand(1e4)]),full_matrices=0)
np.linalg.svd(np.array([arange(1e4),np.random.randn(1e4)]),full_matrices=0)
np.linalg.svd(np.array([arange(1e4),np.random.randn(1e4)]),full_matrices=1)
R = np.random.randn(1e4)
np.linalg.svd(np.array([arange(1e4),R]),full_matrices=0)
np.linalg.svd(np.array([arange(1e4),R]),full_matrices=1)
Out[395][2][-1,:-1]
Out[396][2][-1,:-1]
Out[396][2].shape
Out[396][1].shape
Out[395][2].shape
Out[395][2][-1,:-1]/-Out[395][2][-1,-1]
Out[396][2][-1,:-1]/-Out[396][2][-1,-1]
Out[396][2][0,:-1]/-Out[396][2][-1,-1]
help(np.linalg.svd)
Out[396][2].H
Out[396][2].T
Out[396][1]
Out[395][1]
help(np.linalg.svd)
np.diag(Out[395][1])
Out[395][2].shape
x = arange(1e4)
y = x+R
In[395]
sparse = np.linalg.svd(x,y,full_matrices=0)
sparse = np.linalg.svd([x,y],full_matrices=0)
full = np.linalg.svd([x,y],full_matrices=True)
figure()
plot(x,y)
y = x+R*100
plot(x,y)
y = x+R*1000
plot(x,y)
clf()
plot(x,y)
sparse = np.linalg.svd([x,y],full_matrices=0)
full = np.linalg.svd([x,y],full_matrices=True)
figure()
plot(sparse[2])
plot(sparse[2].T)
clf()
plot(sparse[2].T)
plot(sparse[2][0,:])
plot(full[2][0,:]
)
plot(full[2][-1,:])
full[0].shape
full[1].shape
sparse[0].shape
full[0]
np.dot(full[0],full[1])
np.dot(full[0],np.diag(full[1]))
help(np.linalg.svd)
full[0]
full[1]
sparse[0]
sparse[1]
import scipy.sparse
help(scipy.sparse.linalg.svds)
import scipy.sparse.linalg
help(scipy.sparse.linalg.svds)
import scipy.sparse.linalg.svds
full[2][-1,:-1]/-full[2][-1,-1]
sparse[2][-1,:-1]/-sparse[2][-1,-1]
np.hstack([x,y]).shape
np.vstack([x,y]).shape
scipy.sparse.hstack([x,y]).shape
full = np.linalg.svd(np.vstack([x,y]).T,full_matrices=True)
sparse = np.linalg.svd(np.vstack([x,y]).T,full_matrices=False)
full[2][-1,:-1]/-full[2][-1,-1]
sparse[2][-1,:-1]/-sparse[2][-1,-1]
np.scalar
np.linalg.svd(np.array([arange(1e5),np.random.randn(1e5)]),full_matrices=0)
np.linalg.svd(np.array([arange(1e5),np.random.randn(1e5)]).T,full_matrices=0)
np.linalg.svd(np.array([arange(1e6),np.random.randn(1e6)]).T,full_matrices=0)
len("blasdgasdfasdfa")
206265/400.
206265/415.
206265/18500.
400./206265.
206265/5e4.
206265/5e4
400./206265. * 33
400./206265. * 120
im1
im1 = np.zeros([10,10])
im1[4,4] = 1
im2 = np.zeros([10,10])
im2[5,5] = 1
import AG_image_tools
AG_image_tools.cross_correlation_shifts(im1,im2)
roll 
help(roll)
help(rollaxis)
roll(roll(im1,1,0),1,1)
(roll(roll(im1,1,0),1,1) - im2).sum()
im1[4,4]=0
im1[4,3] = 1
AG_image_tools.cross_correlation_shifts(im1,im2)
(roll(roll(im1,2,0),1,1) - im2).sum()
get_ipython().magic(u"history ")
yoff,xoff = AG_image_tools.cross_correlation_shifts(im1,im2)
im1_aligned_to_im2 = roll(roll(im1,yoff,0),xoff,1)
im1_aligned_to_im2 = roll(roll(im1,yoff,0),xoff,1)
yoff
reload(AG_image_tools)
reload(AG_image_tools.cross_correlation_shifts)
import AG_image_tools.cross_correlation_shifts
reload(AG_image_tools.cross_correlation_shifts)
import AG_image_tools.cross_correlation_shifts
import AG_image_tools.cross_correlation_shifts
import AG_image_tools.cross_correlation_shifts
reload(AG_image_tools.cross_correlation_shifts)
reload(AG_image_tools)
yoff,xoff = AG_image_tools.cross_correlation_shifts(im1,im2)
yoff
get_ipython().magic(u"history ")
