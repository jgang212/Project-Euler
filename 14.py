# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:09:42 2015

@author: jack.gang
"""

import time    

start = time.clock()

def findCollatzLength(n, storedResults):
    length = 1
    while (n != 1):
        # dynamic programming to speed up by factor of 10
        if n in storedResults:
            return length + storedResults[n]
        else:
            if (n % 2 == 0):
                n = n /2
            else:
                n = 3*n + 1
        length += 1
    return length
    
maxLength = 0
answer = 0   
storedLengths = {}              
for i in range(1, 1000000):
    length = findCollatzLength(i, storedLengths)
    storedLengths[i] = length
    if length > maxLength:
        maxLength = length
        answer = i

elapsed = time.clock() - start
                    
print(str(answer) + " found in " + str(elapsed) + " seconds")
