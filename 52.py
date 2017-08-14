# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time  

start = time.clock()

def multipleSameDigits(n):
    originalNum = str(n)
    twoNum = str(2*n)
    threeNum = str(3*n)
    fourNum = str(4*n)
    fiveNum = str(5*n)
    sixNum = str(6*n)
    
    # check if sorted unique digits are the same
    if sorted(set(str(originalNum))) == sorted(set(str(twoNum))) == sorted(set(str(threeNum))) == sorted(set(str(fourNum))) == sorted(set(str(fiveNum))) == sorted(set(str(sixNum))):
        return True
    return False

num = 1
answer = 0
while True:
    if multipleSameDigits(num):
        answer = num
        break
    num += 1
    
elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
