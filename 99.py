# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:09:42 2015

@author: jack.gang
"""

import time  
import math

start = time.clock()

# input text into list of lists
numList = []

f = open('p099_base_exp.txt', 'r')
for line in f:
    numList.append(line.split(sep=","))
f.close()

results = []
for pair in numList:
    # normalize exponents by making base 1 million
    newExp = int(pair[1]) / math.log(1000000, int(pair[0]))
    results.append(newExp)

answer = results.index(max(results)) + 1

elapsed = time.clock() - start
                    
print(str(answer) + " found in " + str(elapsed) + " seconds")
