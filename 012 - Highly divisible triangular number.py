# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:09:42 2015

@author: jack.gang
"""

import time    
import math
from EulerFunctions import countDivisors

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