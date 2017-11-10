# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time  
import math
from EulerFunctions import isPrime

start = time.clock()

answer = 2
primeList = []
while True:
    if isPrime(answer):
        primeList.append(answer)
    elif answer % 2 == 1:
        valid = False
        for prime in primeList: # check primes smaller than number
            if math.sqrt((answer - prime)/2).is_integer():
                valid = True
                break
        if not valid:
            break
    answer += 1

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
