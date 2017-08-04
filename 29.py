# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time    

start = time.clock()

numList = []
for a in range(2, 101):
    for b in range(2, 101):
        result = a**b
        if result not in numList:
            numList.append(result)

answer = len(numList)

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
