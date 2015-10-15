# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:45:23 2015

@author: jack.gang
"""

import math
import time
import string

def checkIfTriangle(n):
    if float((2*n)**0.5).is_integer():
        return False
        
    low = int(math.floor((2*n)**0.5))
    high = int(math.ceil((2*n)**0.5))
    if low * high / 2 == n:
        return True
    return False

start = time.clock()

wordList = []
with open('42_words.txt', 'r') as source:
    for line in source:
        fields = line.split(',')
        wordList.append(fields)
wordList = wordList[0]

values = dict()
for index, letter in enumerate(string.ascii_uppercase):
   values[letter] = index + 1

count = 0
for word in wordList:
    wordSum = 0
    word = word.replace('"', "")
    for letter in word:
        wordSum = wordSum + values[letter]
    if checkIfTriangle(wordSum):
        print word, wordSum
        count = count + 1

answer = count

elapsed = time.clock() - start

print("%s found in %s seconds") % (answer,elapsed)