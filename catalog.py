print "Now running program. Maybe"

import numpy as np
import math 

ra_h, ra_m, ra_s,dec_d, dec_m, dec_s,z_em,z_abs = np.loadtxt("SSA22_LBG.txt", skiprows=1, unpack=True)

ra = 15*(ra_h+ra_m/60+ra_s/3600)
dec = dec_d+dec_m/60+dec_s/3600

here = np.where(((z_em > 2.9) & (z_em < 3.5)) | ((z_abs > 2.9) & (z_abs < 3.5)))
#print ra[here]
n1 = len(ra[here])
n2 = len(dec[here])

ra_f=ra[here[0]]
dec_f=dec[here[0]]

#Begin writing to region file:

#outName= raw_input("Enter output file name: ")
outName= "LBG_RefCat"
f = open(outName, 'w')
for i in xrange(n1):
	f.write(" ("+str(ra_f[i]) + str(dec_f[i]))
f.close()





