# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time    

start = time.clock()

def isPrime(n):
    # trivial cases
    if n <= 1:
        return False
    if n in [2, 3, 5]:
        return True
    if n % 2 == 0:
        return False
    
    # divisibility rules
    # 3
    digitSum = 0
    for digit in str(n):
        digitSum += int(digit)
    if digitSum % 3 == 0:
        return False
    # 5
    if str(n)[-1:] in [0, 5]:
        return False
    
    # hard check
    limit = int(n**0.5)
    for x in range(2, limit+1):
        if n % x == 0:
            return False
    return True

num = 3     # starting number after middle
size = 1000000
diagonalNumIsPrime = []
increment = 2
# doesn't matter which way it spirals
for n in range(3,size+1,2):
    for i in range(0,4):
        diagNum = (num + increment*i)
        diagonalNumIsPrime.append(isPrime(diagNum))
    if (n+1) < size:
        num = num + increment*4 + 2
        increment += 2
    # need to add 1 for "1" in middle of diagonals
    if sum(diagonalNumIsPrime) / (len(diagonalNumIsPrime)+1) < 0.10:
        break

answer = n
            
elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
