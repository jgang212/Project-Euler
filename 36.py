# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time    

start = time.clock()

# convert base 10 to binary (no leading zeroes)
def convertToBinary(n):
    binaryStr = ""
    while n > 0:
        if n % 2 == 0:
            binaryStr = "0" + binaryStr            
        else:
            binaryStr = "1" + binaryStr
        n = n // 2
    return binaryStr

def checkIfPalindrome(numStr):
    for i in range(0, len(numStr)):
        if numStr[i] != numStr[len(numStr)-1-i]:
            return False
        if i >= (len(numStr)-1-i):
            break
    return True

# MAIN
answer = 0
for i in range(1, 1000000):
    if checkIfPalindrome(str(i)) and checkIfPalindrome(str(convertToBinary(i))):
        answer += i

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
