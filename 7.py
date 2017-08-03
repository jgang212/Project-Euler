# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 08:27:27 2015

@author: jack.gang
"""

import time

def isPrime(n):
    limit = int(n**0.5)
    for x in range(limit, 1, -1):
        if n % x == 0:
            return False
    return True

def nthPrime(n):
    number = 2
    count = 0
    while True:
        if isPrime(number):
            count = count + 1
        if count == n:
            return number
        number = number + 1        

start = time.time()

answer = nthPrime(10001)

elapsed = time.time() - start

print("{} found in {} seconds".format(answer,elapsed))