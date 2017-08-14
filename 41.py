# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time  

start = time.clock()

def isPandigital(n):
    for i in range(1, len(str(n))+1):
        if str(i) not in str(n):
            return False
    return True

def isPrime(n):
    # trivial cases
    if n <= 1:
        return False
    if n == 2:
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

# including 8 or 9 makes number divisible by 3
for num in range(7654321, 0, -1):
    if isPandigital(num):
        if isPrime(num):
            answer = num
            break

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
