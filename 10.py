# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 08:57:42 2015

@author: jack.gang
"""

import time
from EulerFunctions import isPrime

def sumOfPrimesBelow(n):
    sum = 0
    for x in range(2, n):
        if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
            continue
        if isPrime(x):
            sum = sum + x
    return sum

start = time.clock()

answer = sumOfPrimesBelow(2000000)

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))