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
