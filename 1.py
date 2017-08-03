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
#    return sum([x for x in range(n) if x % 3 == 0 or x % 5 == 0])
#    return reduce(lambda x,y: x+y, filter(lambda n: n%3==0 or n%5==0, range(1000)))

start = time.clock()

answer = multiple35Sum(1000)

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))