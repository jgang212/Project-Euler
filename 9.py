# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 08:47:19 2015

@author: jack.gang
"""

import time    

start = time.clock()

for b in range(1, 1000):
    a = float(1000.0 * (b - 500.0) / (b - 1000.0))
    if a.is_integer():
        answer = int(a * b * ((a**2 + b**2)**0.5))
        break

elapsed = time.clock() - start

print("%s found in %s seconds") % (answer,elapsed)