# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 13:33:19 2015

@author: jack.gang
"""

import time    
from EulerFunctions import isPrime

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