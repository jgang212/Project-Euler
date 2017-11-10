# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time  
from EulerFunctions import isPrime

start = time.clock()

# list of 4 digit primes
primeList = []
for n in range(1000, 10000):
    if isPrime(n):
        primeList.append(n)

# see which digits have 3 or more prime numbers associated with them
digitPrimeList = {}
for prime in primeList:
    if ''.join(sorted(str(prime))) in digitPrimeList:
        digitPrimeList[''.join(sorted(str(prime)))].append(prime)
    else:
        digitPrimeList[''.join(sorted(str(prime)))] = [prime]

# check for arithmetic sequence
for digits in digitPrimeList:
    primes = digitPrimeList[digits]
    if len(primes) >= 3:
        diffList = []
        for i in range(0, len(primes)):
            for j in range(i+1, len(primes)):
                for k in range(j+1, len(primes)):
                    if (primes[k] - primes[j]) == (primes[j] - primes[i]) and primes[i] != 1487:
                        answer = str(primes[i]) + str(primes[j]) + str(primes[k])

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
