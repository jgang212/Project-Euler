# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time  

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
