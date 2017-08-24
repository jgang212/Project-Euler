# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time

start = time.clock()

def isPandigitalZero(n):
    if len(str(n)) != len(set(str(n))):
        return False
    for i in range(0, len(str(n))):
        if str(i) not in str(n):
            return False
    return True

# 17 already checked for in for loop; 5, 3, and 2 are easier to find than to look through list
def checkProperty(n, divideSevenList, divideElevenList, divideThirteenList):
    divideThirteen = int(str(n)[6:9]) in divideThirteenList
    if not divideThirteen: 
        return False
    divideEleven = int(str(n)[5:8]) in divideElevenList
    if not divideEleven: 
        return False
    divideSeven = int(str(n)[4:7]) in divideSevenList
    if not divideSeven: 
        return False
    divideFive = str(n)[5:6] in ["5", "0"]
    if not divideFive: 
        return False
    divideThree = int(str(n)[2:5]) % 3 == 0
    if not divideThree: 
        return False
    divideTwo = int(str(n)[3:4]) % 2 == 0
    if not divideTwo: 
        return False

    return True

divideSevenList = range(7, 1000, 7)
divideElevenList = range(11, 1000, 11)
divideThirteenList = range(13, 1000, 13)
divideSeventeenList = range(17, 1000, 17)
answer = 0

# only construct first 7 digits, last 3 digits must be divisible by 17
for num in range(1023456, 9876543+1):
    if len(str(num)) == len(set(str(num))) and (str(num)[5] in ["5", "0"]) and (int(str(num)[3]) % 2 == 0):        
        for seventeenMultiple in divideSeventeenList:
            if len(str(seventeenMultiple)) == 2:
                number = int(str(num) + "0" + str(seventeenMultiple))
            else:
                number = int(str(num) + str(seventeenMultiple))
            if isPandigitalZero(number):
                if checkProperty(number, divideSevenList, divideElevenList, divideThirteenList):
                    answer += number
    
elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
