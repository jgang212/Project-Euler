# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:09:42 2015

@author: jack.gang
"""

import time
from EulerFunctions import isPrime#, findPrimeFactors
import numpy as np

start = time.clock()

#def totient(n, primeList):
#    primeFactors = findPrimeFactors(n, primeList)
#    nonTotientList = []
#    for prime in primeFactors:
#        num = prime
#        multiplier = 2
#        while num < n:
#            if num not in nonTotientList:
#                nonTotientList.append(num)
#            num = multiplier*prime
#            multiplier += 1
#    return n - 1 - len(nonTotientList)

primeList = []
answer = 0
# don't actually need to calculate quotient, the n's with the largest quotient are just products of prime numbers
for n in range(2,1000001):
    if isPrime(n):
        primeList.append(n)
    if np.prod(primeList) > 1000000:
        answer = np.prod(primeList[:-1])
        break
#    ratio = n / totient(n, primeList)
#    if ratio > maxRatio:
#        maxRatio = ratio
#        answer = n

elapsed = time.clock() - start
                    
print(str(answer) + " found in " + str(elapsed) + " seconds")
