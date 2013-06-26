########################################################
# Started Logging At: 2012-05-19 09:46:24
########################################################

import idlsave
bgps = idlsave.read('bolocat_v2.0_culled.sav')
bgps.bgps_culled
hist(bgps.bgps_culled.flux_40,bins=50)
hist(bgps.bgps_culled.flux_40,bins=np.logspace(-1,2,50))
clf()
hist(bgps.bgps_culled.flux_40,bins=np.logspace(-1,2,50))
loglog()
hist(bgps.bgps_culled.flux_40,bins=np.logspace(-1,2,50))
import plfit
plfit.plfit(bgps.bgps_culled.flux_40)
P = In[11]
P = Out[11]
O
P
P.kstest_ 
P.alpha_ 
P.plot_lognormal_pdf()
figure()
P.plot_lognormal_pdf()
figure()
P.plotpdf()
P._av
P._ks
P._alpha
P._alphaerr
print P
get_ipython().magic(u"history ")
