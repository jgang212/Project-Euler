# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:09:42 2015

@author: jack.gang
"""

import time
from EulerFunctions import isPrime

start = time.clock()

primeList = []
# we know it has to be larger than 56003 from problem
for n in range(56003,1000000):
    if isPrime(n):
        primeList.append(n)

answer = 0
for num in primeList:
    # replace one digit    
    for digitIndex in range(0, len(str(num))):
        count = 0
        for digit in range(0, 10):
            if digitIndex == 0 and digit == 0:
                continue
            newNum = int(str(num)[:digitIndex] + str(digit) + str(num)[digitIndex+1:])
            if isPrime(newNum):
                count += 1
        if count >= 8:
            answer = int(str(num)[:digitIndex] + str(1) + str(num)[digitIndex+1:])
            break    
    # replace two digits
    for digitIndex1 in range(0, len(str(num))-1):
        for digitIndex2 in range(digitIndex1+1, len(str(num))):
            count = 0
            for digit in range(0, 10):
                if digitIndex1 == 0 and digit == 0:
                    continue
                newNum = int(str(num)[:digitIndex1] + str(digit) + str(num)[digitIndex1+1:digitIndex2] + str(digit) + str(num)[digitIndex2+1:])
                if isPrime(newNum):
                    count += 1
            if count >= 8:
                answer = int(str(num)[:digitIndex1] + str(1) + str(num)[digitIndex1+1:digitIndex2] + str(1) + str(num)[digitIndex2+1:])
                break 
    # replace three digits
    for digitIndex1 in range(0, len(str(num))-2):
        for digitIndex2 in range(digitIndex1+1, len(str(num))-1):
            for digitIndex3 in range(digitIndex2+1, len(str(num))):
                count = 0
                for digit in range(0, 10):
                    if digitIndex1 == 0 and digit == 0:
                        continue
                    newNum = int(str(num)[:digitIndex1] + str(digit) + str(num)[digitIndex1+1:digitIndex2] + str(digit) + str(num)[digitIndex2+1:digitIndex3] + str(digit) + str(num)[digitIndex3+1:])
                    if isPrime(newNum):
                        count += 1
                if count >= 8:
                    answer = int(str(num)[:digitIndex1] + str(1) + str(num)[digitIndex1+1:digitIndex2] + str(1) + str(num)[digitIndex2+1:digitIndex3] + str(1) + str(num)[digitIndex3+1:])
                    break 
    # replace four digits
    for digitIndex1 in range(0, len(str(num))-3):
        for digitIndex2 in range(digitIndex1+1, len(str(num))-2):
            for digitIndex3 in range(digitIndex2+1, len(str(num))-1):
                for digitIndex4 in range(digitIndex3+1, len(str(num))):
                    count = 0
                    for digit in range(0, 10):
                        if digitIndex1 == 0 and digit == 0:
                            continue
                        newNum = int(str(num)[:digitIndex1] + str(digit) + str(num)[digitIndex1+1:digitIndex2] + str(digit) + str(num)[digitIndex2+1:digitIndex3] + str(digit) + str(num)[digitIndex3+1:digitIndex4] + str(digit) + str(num)[digitIndex4+1:])
                        if isPrime(newNum):
                            count += 1
                    if count >= 8:
                        answer = int(str(num)[:digitIndex1] + str(1) + str(num)[digitIndex1+1:digitIndex2] + str(1) + str(num)[digitIndex2+1:digitIndex3] + str(1) + str(num)[digitIndex3+1:digitIndex4] + str(1) + str(num)[digitIndex4+1:])
                        break 
    if answer > 0:
        break                        

elapsed = time.clock() - start
                    
print(str(answer) + " found in " + str(elapsed) + " seconds")
