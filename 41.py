# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time  
from EulerFunctions import isPrime, isPandigital

start = time.clock()

# including 8 or 9 makes number divisible by 3
for num in range(7654321, 0, -1):
    if isPandigital(num):
        if isPrime(num):
            answer = num
            break

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
