# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 13:33:19 2015

@author: jack.gang
"""

import time    

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(n**0.5)
    for x in range(2, limit+1):
        if n % x == 0:
            return False
    return True

def rotate(n):
    return str(n)[len(str(n))-1] + str(n)[:len(str(n))-1]

start = time.clock()

count = 0
for x in range(100, 1000000):
    stop = False
    if not isPrime(x):
        continue
    newX = x
    for i in range(0, len(str(x))-1):
        newX = int(rotate(newX))
        if not isPrime(newX):
            stop = True
            continue  
    if stop:
        continue
    #print x
    count = count + 1

answer = count + 13

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))