# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time    
import math
#from EulerFunctions import factorial

start = time.clock()

answer = 0
# 2177281 is 9! * 6 digits, can't be higher than this
for i in range(1, 2177281):
    factSum = 0
    for digit in str(i):
        fact = math.factorial(int(digit))
        factSum += fact
    if factSum == i and (i not in [1, 2]):
        #print(i)
        answer += i

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
