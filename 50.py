# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time  
from EulerFunctions import isPrime

start = time.clock()

# find primes under a million first
primeList = []
for num in range(1, 1000000):
    if isPrime(num):
        primeList.append(num)

# find the longest possible consecutive sequence sum under a million (if we started at 2)
maxLength = 0
for n in range(1, len(primeList)):
    if sum(primeList[0:n]) > 1000000:
        maxLength = n - 1
        break

answer = 0
n = 0       # increment starting index
while True:
    if sum(primeList[n:maxLength+n]) < 1000000:
        if sum(primeList[n:maxLength+n]) in primeList:
            answer = sum(primeList[n:maxLength+n])
            break
        else:
            n += 1
    # reset starting index, shorten length by 1
    else:
        n = 0
        maxLength -= 1

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
