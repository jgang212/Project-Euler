# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time  

start = time.clock()

asciiList = []
f = open('p059_cipher.txt', 'r')
for line in f:
    asciiList = line.split(sep=",")
f.close()

# the result that has the highest % of spaces is probably the correct answer
spacePerc = 0
resultList = []
# 97 to 122 represent lower case letters
for key1 in range(97, 123):
    for key2 in range(97, 123):
        for key3 in range(97, 123):
            result = ""
            numSpaces = 0
            for i in range(0, len(asciiList)):  
                # use key1
                if i % 3 == 0:
                    decrypted = int(asciiList[i])^key1
                # use key2
                elif i % 3 == 1:
                    decrypted = int(asciiList[i])^key2
                # use key3
                else:
                    decrypted = int(asciiList[i])^key3
                                   
                result += chr(decrypted)
                # check if space
                if decrypted == 32:
                    numSpaces += 1
            
            if (numSpaces / len(asciiList)) > spacePerc:  
                spacePerc = numSpaces / len(asciiList)
                asciiSum = 0
                for i in range(0, len(asciiList)):  
                    # use key1
                    if i % 3 == 0:
                        asciiSum += ord(result[i])
                    # use key2
                    elif i % 3 == 1:
                        asciiSum += ord(result[i])
                    # use key3
                    else:
                        asciiSum += ord(result[i])
                resultList.append(asciiSum)

answer = resultList[-1:][0]

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
