# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 08:22:40 2015

@author: jack.gang
"""

import time

def isPrime(n):
    limit = int(n**0.5)
    for x in range(limit, 1, -1):
        if n % x == 0:
            return False
    return True

def largestPrimeFactor(n):
    limit = int(n**0.5)
    for x in range(limit, 1, -1):
        if n % x == 0:
            if isPrime(x):
                return x
    return False
    
start = time.time()

answer = largestPrimeFactor(600851475143)

elapsed = time.time() - start

print("%s found in %s seconds") % (answer,elapsed)