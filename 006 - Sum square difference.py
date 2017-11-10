# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:59:41 2015

@author: jack.gang
"""

import time

def sumOfSquares(n):
    totalSum = 0
    for x in range(1,n+1):
        totalSum += x*x
    return totalSum

def squareOfSum(n):
    totalSum = 0
    for x in range(1,n+1):
        totalSum += x
    return totalSum*totalSum

start = time.time()

answer = squareOfSum(100) - sumOfSquares(100)

elapsed = time.time() - start

print("{} found in {} seconds".format(answer,elapsed))