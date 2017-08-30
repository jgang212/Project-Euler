# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:24:57 2015

@author: jack.gang
"""

import time

start = time.time()

def checkBouncy(n):
    # check not increasing
    increasing = True
    compareDigit = int(str(n)[0])
    for digit in str(n):
        if int(digit) < compareDigit:
            increasing = False
            break
        else:
            compareDigit = int(digit)
    
    if increasing:
        return False
    
    # check not decreasing
    decreasing = True
    compareDigit = int(str(n)[0])
    for digit in str(n):
        if int(digit) > compareDigit:
            decreasing = False
            break
        else:
            compareDigit = int(digit)
    
    if decreasing:
        return False
    return True

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
 