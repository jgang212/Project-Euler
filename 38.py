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

answer = 0
# we know it has to start with 9 from examples, and can't be more than 4 digits since n > 1
for num in range(9876, 0, -1):
    if str(num)[0] != '9':
        continue
    concatenated = str(num) + str(num*2)
    multiple = 3
    while len(concatenated) < 9:
        concatenated = concatenated + str(num*3)
        multiple += 1
    if len(concatenated) == 9:
        if isPandigital(int(concatenated)):
            if int(concatenated) > answer:
                answer = int(concatenated)
    
elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
