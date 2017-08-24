# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time    
from EulerFunctions import isPrime

start = time.clock()

num = 3     # starting number after middle
size = 1000000
diagonalNumIsPrime = []
increment = 2
# doesn't matter which way it spirals
for n in range(3,size+1,2):
    for i in range(0,4):
        diagNum = (num + increment*i)
        diagonalNumIsPrime.append(isPrime(diagNum))
    if (n+1) < size:
        num = num + increment*4 + 2
        increment += 2
    # need to add 1 for "1" in middle of diagonals
    if sum(diagonalNumIsPrime) / (len(diagonalNumIsPrime)+1) < 0.10:
        break

answer = n
            
elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
