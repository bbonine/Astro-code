import numpy as np 
import math
#config InlineBackend.rc = {}
import matplotlib
matplotlib.rc_file("matplotlibrc")
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
np.set_printoptions(threshold=np.inf)

from astropy.io import fits
image_file = '/Users/Brett/Desktop/Research/ssa22/data2/Mosaic_North_drz_sci.fits'
hdu_list = fits.open(image_file)
image_data = hdu_list[0].data
hdu_list.close()


y,x = np.loadtxt("SSA22_XRAY_XY.txt", skiprows=0, unpack = True)
n1 = len(x)     
n2 = len(y)

xcord = x[0]
ycord = y[0]


with PdfPages('XRAY_Thumbnails.pdf') as pdf:
	for i in xrange(n1):
		subimage = image_data[x[i]-20:x[i]+20,y[i]-20:y[i]+20]
		subimage2 = subimage + math.fabs(np.min(subimage))+1
		plt.imshow(subimage2, cmap='hot', vmin=1, vmax=1.6, norm=LogNorm(), interpolation='nearest')
		plt.subplot(6,6, i+1)
		plt.axis('off')
		

plt.show()	
#plt.close()
		








	
	