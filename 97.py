# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time  

start = time.clock()

#startNum = "00002"
#digitLength = 6
#repeatingDigits = []
#while True:
#    if startNum in repeatingDigits:
#        break
#    else:
#        appendDigits = startNum        
#        repeatingDigits.append(appendDigits)
#        startNum = str(int(startNum) * 2)
#        if len(startNum) > digitLength:
#            startNum = startNum[-digitLength:]
#        if len(startNum) < digitLength:
#            startLength = len(startNum)
#            for i in range(0, digitLength-startLength):
#                startNum = "0" + startNum
#
#startExponent = 7830457
#remainder = (startExponent - 5) % (len(repeatingDigits) - 5)
#digits = repeatingDigits[remainder + 4]
#
#answer = int(digits) * 28433 + 1
#print(digits)

# repeating sequences are of length
# mod 10: 4
# mod 100: 20
# mod 1000: 100
# mod 10000: 500
# mod 100000: 2500
# mod 1000000: 12500
# mod 10000000: 62500
# mod 100000000: 312500
# mod 1000000000: 1562500
# mod 10000000000: 7812500

remainder = 7830457 - 7812500
answer = (28433*2**(remainder)+1) % 10000000000

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))

#2^6
#2^12506
#2^25006