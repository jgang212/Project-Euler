# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:09:42 2015

@author: jack.gang
"""

import time    
from EulerFunctions import round_down

start = time.clock()

numberLengthDict = {}
# there are the unique words <= 1000
numberLengthDict[1] = 3
numberLengthDict[2] = 3
numberLengthDict[3] = 5
numberLengthDict[4] = 4
numberLengthDict[5] = 4
numberLengthDict[6] = 3
numberLengthDict[7] = 5
numberLengthDict[8] = 5
numberLengthDict[9] = 4
numberLengthDict[10] = 3
numberLengthDict[11] = 6
numberLengthDict[12] = 6
numberLengthDict[13] = 8
numberLengthDict[14] = 8
numberLengthDict[15] = 7
numberLengthDict[16] = 7
numberLengthDict[17] = 9
numberLengthDict[18] = 8
numberLengthDict[19] = 8
numberLengthDict[20] = 6
numberLengthDict[30] = 6
numberLengthDict[40] = 5
numberLengthDict[50] = 5
numberLengthDict[60] = 5
numberLengthDict[70] = 7
numberLengthDict[80] = 6
numberLengthDict[90] = 6
numberLengthDict[100] = 10
numberLengthDict[1000] = 11
     
answer = 0
for i in range(1,1001):
    if i in numberLengthDict:
        answer += numberLengthDict[i]
    elif i < 100:
        result = numberLengthDict[round_down(i, 10)] + numberLengthDict[i % 10] # tens + ones
        # store for dynamic programming
        numberLengthDict[i] = result
        answer = answer + result
    elif i < 1000:
        result = numberLengthDict[round_down(i, 100)/100] + 7   # hundreds + "hundred"
        answer = answer + result
        if i % 100 > 0:
            result = result + 3 + numberLengthDict[i % 100]     # + "and" + < 100 portion
            answer = answer + 3 + numberLengthDict[i % 100]
        # store for dynamic programming
        numberLengthDict[i] = result
        
elapsed = time.clock() - start
                    
print(str(answer) + " found in " + str(elapsed) + " seconds")
