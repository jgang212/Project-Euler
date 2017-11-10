# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:23:13 2015

@author: jack.gang
"""

import time
import string

start = time.clock()

wordList = []
with open('22_names.txt', 'r') as source:
    for line in source:
        fields = line.split(',')
        wordList.append(fields)
wordList = wordList[0]

values = dict()
for index, letter in enumerate(string.ascii_uppercase):
   values[letter] = index + 1

wordList.sort()

totalScore = 0
for index, word in enumerate(wordList):
    wordSum = 0
    word = word.replace('"', "")
    for letter in word:
        wordSum = wordSum + values[letter]
    totalScore = totalScore + (index + 1) * wordSum

answer = totalScore

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))