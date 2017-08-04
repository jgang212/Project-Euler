# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time    

start = time.clock()

num = 3     # starting number after middle
size = 1001
diagonalNums = []
increment = 2
for n in range(3,size+1,2):
    for i in range(0,4):
        diagonalNums.append((num + increment*i))
    if (n+1) < size:
        num = num + increment*4 + 2
        increment += 2

answer = sum(diagonalNums)+1
            
elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
