# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:24:57 2015

@author: jack.gang
"""

import time
import math
    
start = time.time()

def factorialChain(n):
    result = 0
    for digit in str(n):
        result += math.factorial(int(digit))
    return result

answer = 0
for n in range(1, 1000000):
    # if 2nd number contains these 6 digits, chain will end in 60
    if ''.join(sorted(str(factorialChain(n)))) == "345679":
        answer += 1
#    existingChainValues = [n]
#    newValue = factorialChain(n)
#    while newValue not in existingChainValues:
#        existingChainValues.append(newValue)
#        newValue = factorialChain(newValue)
#    if len(existingChainValues) == 60:
#        secondValue.append(existingChainValues[1])
#        answer += 1

elapsed = time.time() - start

print("{} found in {} seconds".format(answer,elapsed))
 