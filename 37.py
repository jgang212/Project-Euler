# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time    

start = time.clock()

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(n**0.5)
    for x in range(2, limit+1):
        if n % x == 0:
            return False
    return True

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
