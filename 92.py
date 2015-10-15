# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

# takes two minutes, not good enough

import time    

start = time.clock()

count = 0
for x in range(1, 10000001):
    value = x
    while True:
        if value == 44 or value == 32 or value == 13 or value == 10 or value == 1:
            break
        if value == 85 or value == 89 or value == 145 or value == 42 or value == 20 or value == 4 or value == 16 or value == 37 or value == 58:
            count = count + 1
            break
        newValue = 0
        for digit in str(value):
            newValue = newValue + int(digit)**2
        value = newValue

answer = count

elapsed = time.clock() - start

print("%s found in %s seconds") % (answer,elapsed)