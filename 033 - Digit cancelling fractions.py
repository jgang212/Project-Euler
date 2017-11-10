# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time  
import math  

start = time.clock()

numerator = 1
denominator = 1
for a in range(10, 100):
    for b in range(a+1, 100):   # a+1 guarantees fraction < 1
        for digit in str(a):
            if (digit in str(b)) and (digit != "0"):    # non-trivial cases
                if str(a)[0] == str(a)[1]:      # if digits are equal
                    cancelledA = int(str(a)[0])
                else:
                    cancelledA = int(str(a).replace(digit, ""))
                if str(b)[0] == str(b)[1]:      # if digits are equal
                    cancelledB = int(str(b)[0])
                else:
                    cancelledB = int(str(b).replace(digit, ""))
                if cancelledB != 0:
                    if (a / b) == (cancelledA / cancelledB):
                        numerator *= a
                        denominator *= b

divisor = math.gcd(numerator, denominator)
answer = denominator / divisor

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
