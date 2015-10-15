# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 08:57:42 2015

@author: jack.gang
"""

import time    

def isPrime(n):
    if n <= 1:
        return False
    limit = int(n**0.5)
    for x in range(2, limit+1):
        if n % x == 0:
            return False
    return True

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

print("%s found in %s seconds") % (answer,elapsed)