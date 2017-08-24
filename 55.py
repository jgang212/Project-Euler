# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time  
from EulerFunctions import checkIfPalindrome

start = time.clock()

def reverseAdd(n):
    return int(str(n)[::-1]) + n

answer = 0
# 1 through 4 are trivial non-Lychrel numbers
for num in range(5, 10000):
    startNum = num
    for i in range(0, 50):
        startNum = reverseAdd(startNum)
        if checkIfPalindrome(startNum):
            break
    if i == 49:
        answer += 1

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
