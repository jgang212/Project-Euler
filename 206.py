# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:24:57 2015

@author: jack.gang
"""

import time
from EulerFunctions import round_down
    
start = time.time()

startNum = int(round_down(1020304050607080900**0.5, 10))
endNum = int(round_down(1929394959697989900**0.5, 10))    #if square ends in 0, it has to end in 00, and number has to end with 0
# if square ends in 900, 2nd to last digit of number has to be 3 or 7
startNum1 = startNum
startNum2 = startNum
while str(startNum1)[8] not in ['3']:
    startNum1 += 10
while str(startNum2)[8] not in ['7']:
    startNum2 += 10
while str(endNum)[8] not in ['3', '7']:
    endNum -= 10

answer = 0
for n in range(startNum1, endNum+1, 100):
    square = n**2
    found = True
    for i in range(9, 0, -1):
        if str(square)[2*(i-1)] != str(i):
            found = False
            break
    if found:
        answer = n
        break
if answer == 0:
    for n in range(startNum2, endNum+1, 100):
        square = n**2
        found = True
        for i in range(9, 0, -1):
            if str(square)[2*(i-1)] != str(i):
                found = False
                break
        if found:
            answer = n
            break

elapsed = time.time() - start

print("{} found in {} seconds".format(answer,elapsed))
 