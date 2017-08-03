# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:58:33 2015

@author: jack.gang
"""

import time

def sumOfDigits(n):
    str_n = str(n)
    totalSum = 0
    for x in range(0, len(str_n)):
        totalSum = totalSum + int(str_n[x])
    return totalSum

start = time.time()

answer = sumOfDigits(2**1000)

elapsed = time.time() - start

print("{} found in {} seconds".format(answer,elapsed))