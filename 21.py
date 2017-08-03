# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:09:42 2015

@author: jack.gang
"""

import time  
import math

start = time.clock()

def findDivisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n))+1):
        if (n % i == 0):
            divisors.append(i)
            if (i != 1) and (int(n / i) not in divisors):
                divisors.append(int(n / i))
    return sorted(divisors)

divisorSums = {}
# find all divisor sums under 10000
for i in range(1, 10000):
    divisorSums[i] = sum(findDivisors(i))

answerList = []
# find amicable pairs
for i in range(1, 10000):
    if (divisorSums[i] != i) and (divisorSums[i] < 10000):
        if (divisorSums[divisorSums[i]] == i) and (i not in answerList):
            print(i, divisorSums[i])
            answerList.append(i)
            answerList.append(divisorSums[i])

answer = sum(answerList)

elapsed = time.clock() - start
                    
print(str(answer) + " found in " + str(elapsed) + " seconds")
