# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:09:42 2015

@author: jack.gang
"""

import time    
import math

def countDivisors(n):
    count = 0
    limit = int(math.floor(n**0.5))
    for x in range(1, limit+1):
        if n % x == 0:
            count = count + 1
    count = count * 2
    if float(n**0.5).is_integer():
        count = count - 1
    return count

start = time.clock()

index = 1
triangle = 0
while True:
    triangle = triangle + index
    if triangle % 2 == 1:
        index = index + 1
        continue
    if countDivisors(triangle) > 500:
        answer = triangle
        break
    index = index + 1

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))