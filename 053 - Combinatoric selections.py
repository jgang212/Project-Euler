# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time  
import math

start = time.clock()

answer = 0
# brute force solution, don't need to check nCn or nC1
for n in range(23, 101):
    for r in range(2, n):
        if (math.factorial(n) / (math.factorial(r) * math.factorial(n-r))) > 1000000:
            answer += 1

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
