# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time  

start = time.clock()

answerList = []
for a in range(1, 9877):
    if ("0" in str(a)) or (len(str(a)) != len(set(str(a)))):    # can't contain zero or duplicates
        continue
    for b in range(1,10000 // a):   # product has to be 4 digits, so can stop b at 10000 / a 
        if ("0" in str(b)) or (len(str(b)) != len(set(str(b)))):    # can't contain zero or duplicates
            continue
        valid = True
        for digit in str(b):
            if digit in str(a):
                valid = False
                break
        if valid:
            product = a * b
            if ("0" in str(product)) or (len(str(product)) != len(set(str(product)))):  # can't contain zero or duplicates
                continue
            validAgain = True
            for digit in str(product):
                if (digit in str(a)) or (digit in str(b)):
                    validAgain = False
                    break
            if validAgain:
                if len(str(a) + str(b) + str(product)) == 9:
                    if product not in answerList:
                        print(a, b, product)
                        answerList.append(product)

answer = sum(answerList)
elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
