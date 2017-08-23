# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time  

start = time.clock()

# pattern is n_i = n_i-1 * 2 + n_i-2
numList = [3,7]
denomList = [2,5]

answer = 0
for i in range(1, 999):
    numerator = numList[i]*2+numList[i-1]
    denominator = denomList[i]*2+denomList[i-1]
    
    if len(str(numerator)) > len(str(denominator)):
        answer += 1
    
    numList.append(numerator)
    denomList.append(denominator)

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
