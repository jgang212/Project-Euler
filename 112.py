# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:24:57 2015

@author: jack.gang
"""

import time
from EulerFunctions import checkBouncy

start = time.time()

notBouncyList = []
num = 1
while True:
    if len(str(num)) < 3:
        notBouncyList.append(num)        
    elif not checkBouncy(num):
        notBouncyList.append(num)
    
    if (num - len(notBouncyList)) / num >= 0.99:
        break
    
    num += 1

answer = num

elapsed = time.time() - start

print("{} found in {} seconds".format(answer,elapsed))
 