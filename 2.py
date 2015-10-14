# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:47:25 2015

@author: jack.gang
"""

import time

def fibEven():
    totalSum = 0
    prevX = 0
    x = 1
    while True:
        if x == 1:
            x = 2
            prevX = 1
        else:
            tempX = x
            x = x + prevX
            prevX = tempX
        if x > 4000000:
            break
        if (x % 2 == 0):
            totalSum += x
    return totalSum

start = time.time()

answer = fibEven()

elapsed = time.time() - start

print("%s found in %s seconds") % (answer,elapsed)