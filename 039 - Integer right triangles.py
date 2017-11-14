# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time    
import math

start = time.clock()

triangleList = []
squareList = []
for i in range(1, 999):  # perfect squares under 999^2
    squareList.append(i*i)

side1 = 1
side2 = 1

while True:
    side2 = side1
    if (math.sqrt(side1*side1 + side2*side2) + side1 + side2) > 1000:
        break
    while True:
        if (math.sqrt(side1*side1 + side2*side2) + side1 + side2) > 1000:
            break
        elif (side1*side1 + side2*side2) in squareList:
            triangleList.append(side1 + side2 + int(math.sqrt(side1*side1 + side2*side2)))
        side2 += 1
    side1 += 1

answer = max(set(triangleList), key=triangleList.count)

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
