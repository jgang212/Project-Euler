# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time    

start = time.clock()

count = 0
# we know from problem that these numbers will cause a break or a count
breakValues = [44, 32, 13, 1, 10]
countValues = [85, 89, 145, 42, 20, 4, 16, 37, 58]
lookUp = {}
for x in range(1, 10000000):
    value = x
    while True:
        if value in breakValues:
            break
        elif value in countValues:
            count = count + 1
            break
        elif value in lookUp:
            while lookUp[value] in lookUp:
                value = lookUp[value]
            value = lookUp[value]
        else:
            newValue = 0
            for digit in str(value):
                newValue = newValue + int(digit)**2
            lookUp[x] = newValue        # store for dynamic programming
            value = newValue

answer = count

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))