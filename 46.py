# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time  
import math

start = time.clock()

def isPrime(n):
    # trivial cases
    if n <= 1:
        return False
    if n in [2, 3, 5]:
        return True
    if n % 2 == 0:
        return False
    
    # divisibility rules
    # 3
    digitSum = 0
    for digit in str(n):
        digitSum += int(digit)
    if digitSum % 3 == 0:
        return False
    # 5
    if str(n)[-1:] in [0, 5]:
        return False
    
    # hard check
    limit = int(n**0.5)
    for x in range(2, limit+1):
        if n % x == 0:
            return False
    return True

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
