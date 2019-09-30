import numpy as np
import math 
import matplotlib
from astropy.io import fits


#Import image source positions:
y, x = np.loadtxt("ssa22_XY.reg", skiprows=0, unpack = True)
segmap = '/Users/Brett/Desktop/Research/ssa22/Code/check.fits'
image = '/Users/Brett/Desktop/Research/ssa22/Code/Mosaic_North2_drz_sci.fits'

hdulist_seg = fits.open(segmap)
hdulist_img = fits.open(image)


seg_data = hdulist_seg[0].data
img_data = hdulist_img[0].data


n1 = len(x)


M=0

for i in xrange(n1):
		source = seg_data[x[i],y[i]]
		if source != 0:
			
			here = np.where( seg_data == source)
			flux = img_data[here]
			
			g=0
			for j in range(n):
				M_j= flux[j]((seg_data[x[i]
				g = g+g_j
			g = g/(avg*n*(n-1))
			print g