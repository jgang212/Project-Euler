# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:09:42 2015

@author: jack.gang
"""

import time    

start = time.clock()

accumulatedSum = 0
f = open('13.txt', 'r')
for line in f:
    # only need a few extra digits past the first 10
    accumulatedSum += int(line[0:15])
f.close()

answer = str(accumulatedSum)[0:10]

elapsed = time.clock() - start

print(answer + " found in " + str(elapsed) + " seconds")