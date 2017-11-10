# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time    
from EulerFunctions import convertToBinary, checkIfPalindrome

start = time.clock()

# MAIN
answer = 0
for i in range(1, 1000000):
    if checkIfPalindrome(str(i)) and checkIfPalindrome(convertToBinary(i)):
        answer += i

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
