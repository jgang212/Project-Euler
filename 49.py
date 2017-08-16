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
