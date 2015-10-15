# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:53:52 2015

@author: jack.gang
"""

import time    

start = time.clock()

totalSum = 0
prevX = 0
x = 1
index = 2
while True:
    if x == 1:
        x = 2
        prevX = 1
        index = index + 1
    else:
        tempX = x
        x = x + prevX
        prevX = tempX
        index = index + 1
    if len(str(x)) == 1000:
        answer = index      
        break

elapsed = time.clock() - start

print("%s found in %s seconds") % (answer,elapsed)