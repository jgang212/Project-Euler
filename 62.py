# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:09:42 2015

@author: jack.gang
"""

import time  
import math

start = time.clock()

answer = 0
i = 0
while True:
    initialCube = i**3
    smallestNum = int(''.join(sorted(str(initialCube))))
    largestNum = int(''.join(sorted(str(initialCube), reverse=True)))
    # find range of cubes using digits
    if largestNum**(1/3) - smallestNum**(1/3) < 4:
        i += 1
        continue
    else:
        count = 0
        for j in range(math.ceil(smallestNum**(1/3)), math.ceil(largestNum**(1/3))):
            otherCube = j**3
            if sorted(str(otherCube)) == sorted(str(initialCube)):
                count += 1
        if count == 5:
            answer = initialCube
            break
        i += 1

elapsed = time.clock() - start
                    
print(str(answer) + " found in " + str(elapsed) + " seconds")
