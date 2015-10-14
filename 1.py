# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:40:12 2015

@author: jack.gang
"""

import time

def multiple35Sum(n):
    totalSum = 0
    for x in range(1,n):
        if (x % 3 == 0) or (x % 5 == 0):
            totalSum += x
    return totalSum

start = time.time()

answer = multiple35Sum(1000)

elapsed = time.time() - start

print("%s found in %s seconds") % (answer,elapsed)