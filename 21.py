# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:09:42 2015

@author: jack.gang
"""

import time  
import math
from EulerFunctions import findDivisors

start = time.clock()

divisorSums = {}
# find all divisor sums under 10000
for i in range(1, 10000):
    divisorSums[i] = sum(findDivisors(i))

answerList = []
# find amicable pairs
for i in range(1, 10000):
    if (divisorSums[i] != i) and (divisorSums[i] < 10000):
        if (divisorSums[divisorSums[i]] == i) and (i not in answerList):
            #print(i, divisorSums[i])
            answerList.append(i)
            answerList.append(divisorSums[i])

answer = sum(answerList)

elapsed = time.clock() - start
                    
print(str(answer) + " found in " + str(elapsed) + " seconds")
