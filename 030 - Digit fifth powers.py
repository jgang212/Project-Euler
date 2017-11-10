# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time    

start = time.clock()

answerList = []
# 9^5 * 6 = 354294, so we can stop checking at this number
for num in range(10, 354295):
    powerSum = 0
    for digit in str(num):
        powerSum += int(digit)**5
    if powerSum == num:
        answerList.append(num)

answer = sum(answerList)

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
