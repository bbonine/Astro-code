print "Now running the Region File Maker. Hopefully"

import numpy as np
import math 

inName= raw_input("Enter name of catalog file:")
ra_h, ra_m, ra_s,dec_d, dec_m, dec_s,z_em,z_abs = np.loadtxt(inName, skiprows=1, unpack=True)

ra = 15*(ra_h+ra_m/60+ra_s/3600)
dec = dec_d+dec_m/60+dec_s/3600

here = np.where(((z_em > 2.9) & (z_em < 3.5)) | ((z_abs > 2.9) & (z_abs < 3.5)))
#print ra[here]
n1 = len(ra[here])
n2 = len(dec[here])

ra_f=ra[here[0]]
dec_f=dec[here[0]]

#Begin writing to region file:

outName= raw_input("Enter desired Region file name: ")
f = open(outName, 'w')
f.write("global color = cyan\n")
for i in xrange(n1):
	f.write("fk5;circle(" +str(ra_f[i]) + "," + str(dec_f[i]) + ",2.0" + "\")\n")
f.close()


print "Region File successfully written!"





