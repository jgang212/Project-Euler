# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time  
from EulerFunctions import isPrime

start = time.clock()

def countDistinctPrimeFactors(n, primeList):
    count = 0
    for prime in primeList:
        if num % prime == 0:
            count += 1
    return count

# can start at 647
primeList = []
for n in range(2, 647):
    if isPrime(n):
        primeList.append(n)

num = 647
numList = []
while True:
    if isPrime(num):
        primeList.append(num)
    else:
        if len(numList) == 0:
            if countDistinctPrimeFactors(num, primeList) == 4:
                numList.append(num)
        else:
            # don't need to check prime factors if not consecutive
            if num - numList[len(numList)-1] == 1:
                if countDistinctPrimeFactors(num, primeList) == 4:
                    numList.append(num)
            else:
                numList.clear()
    if len(numList) == 4:
        answer = numList[0]
        break
    num += 1

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
