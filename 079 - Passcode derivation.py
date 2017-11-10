# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time  

start = time.clock()

successList = []
f = open('p079_keylog.txt', 'r')
for line in f:
    successList.append(line.split()[0])
f.close()

# only care about unique attempts
successList = set(successList)

answer = ''
for attempt in successList:
    if answer == '':
        answer += attempt
    else:
        insertedOne = False
        insertedThree = False
        # place first digit in front if doesn't yet exist
        if attempt[0] not in answer:
            answer = attempt[0] + answer
            insertedOne = True
        # place last digit in back if doesn't yet exist
        elif attempt[2] not in answer:
            answer = answer + attempt[2]
            insertedThree = True
        # place middle digit next to 1st or 3rd digit if they exist
        elif attempt[1] not in answer:
            if insertedOne:
                answer = answer[:1] + attempt[1] + answer[1:]
            elif insertedThree:
                answer = answer[:-1] + attempt[1] + answer[-1:]
            else:
                answer = answer[:-answer.index(attempt[0])] + attempt[1] + answer[-answer.index(attempt[0]):]
        # swap existing letters if necessary
        else:
            if answer.index(attempt[0]) > answer.index(attempt[1]):       
                answerList = list(answer)
                answerList[answer.index(attempt[0])], answerList[answer.index(attempt[1])] = answerList[answer.index(attempt[1])], answerList[answer.index(attempt[0])]
                answer = ''.join(answerList)
            if answer.index(attempt[1]) > answer.index(attempt[2]):     
                answerList = list(answer)
                answerList[answer.index(attempt[1])], answerList[answer.index(attempt[2])] = answerList[answer.index(attempt[2])], answerList[answer.index(attempt[1])]
                answer = ''.join(answerList)         

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
