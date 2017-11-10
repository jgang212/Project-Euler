# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time   
from EulerFunctions import isPrime 

start = time.clock()

count = 0
checkNum = 10
primeList = [2, 3, 5, 7]    # don't need to check truncated for isPrime since they are all smaller and will be in this list
answerList = []
while count < 11:
    if isPrime(checkNum):
        primeList.append(checkNum)
        counted = True
        for i in range(1, len(str(checkNum))):
            if int(str(checkNum)[i:]) not in primeList:
                counted = False
                break
            if int(str(checkNum)[:i]) not in primeList:
                counted = False
                break
        if counted:
            count += 1
            answerList.append(checkNum)
    checkNum += 1

answer = sum(answerList)

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
