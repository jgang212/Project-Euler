# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:24:57 2015

@author: jack.gang
"""

import time

def factorialSum(n):
    new = 1
    for x in range(1, n+1):
        new = x * new
    final= 0
    while new:        
        digit = new % 10
        new = new // 10
        final += digit
    return final
    
start = time.time()

answer = factorialSum(100)

elapsed = time.time() - start

print("{} found in {} seconds".format(answer,elapsed))
 