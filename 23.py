# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time    
import math

start = time.clock()

def isAbundant(n):
    divisors = []
    for i in range(1, int(math.sqrt(n))+1):
        if (n % i == 0):
            divisors.append(i)
            if (i != 1) and (int(n / i) not in divisors):
                divisors.append(int(n / i))
    return sum(divisors) > n

abundantList = []
abundantListOdd = []
for i in range(1, 28124):
    if (isAbundant(i)):
        if (i % 2 == 1):
            abundantListOdd.append(i)
        abundantList.append(i)
        
                    
abundantSums= []
# after the first 6 numbers, all even+even sums are accounted for
for i in range(0, 7):
    for j in range(i, len(abundantList)):
        newSum = abundantList[i] + abundantList[j]
        if (newSum not in abundantSums) and (newSum <= 28123):
            abundantSums.append(newSum)

for i in range(24, 28124):
    if i not in abundantSums:
        for num in abundantListOdd: # look only in odd list
            if num > (i - 12):
                break
            elif (i - num) in abundantList:
                abundantSums.append(i)
                break
                    
answer = sum(range(1, 28124)) - sum(abundantSums)

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))