# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time    

start = time.clock()

def isInfiniteDenominator(n):
    divided = n
    # if there are only prime factors of 2 and 5 in denominator, then finite decimal
    while True:
        if divided % 2 == 0:
            divided /= 2
        elif divided % 5 == 0:
            divided /= 5
        elif divided == 1:
            return False
        else:
            return True

# use long division and then find previous remainder
def findRepeatingDecimal(num, denom):
    rem = num
    prevRems = [rem]
    while rem != 0:
        if rem < denom:
            rem *= 10
        rem = rem % denom
        if rem in prevRems:
            return len(prevRems[prevRems.index(rem):])
        else:
            prevRems.append(rem)
    return False

infiniteList = []
for i in range(1,1000):
    if isInfiniteDenominator(i):
        infiniteList.append(i)
   
maxLength = 0     
answer = 0
for num in infiniteList:
    length = findRepeatingDecimal(1, num)
    if length > maxLength:
        answer = num
        maxLength = length

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))