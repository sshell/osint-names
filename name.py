###         name.py [name] [m/f]         ###
###   spanning 138 years : 1880 - 2017   ###

import os
import sys
import numpy as np
import matplotlib.pylab as plt

fol = 'namedata'
d = {}

nm = sys.argv[1].title()
sx = sys.argv[2].upper()

combo = nm + ',' + sx
cl = len(combo)+1

for file in os.listdir(fol):
    with open(fol+'/'+file, 'r') as f:
        for line in f:
            if combo in line:
                year = file[3:7]
                d[year] = line[cl:]
        
yr = list(map(int, d.keys()))
fr = list(map(int, d.values()))

plt.title('popularity of the name '+ nm +' ('+ sx +') over time')
plt.plot(yr,fr)
#plt.yscale('log')     # switch to log scaling
plt.show()
