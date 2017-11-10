# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time  

start = time.clock()

# first nine postiive integers all follow this trivially
answer = 9

digits = 2
while True:
    done = False
    i = 1
    # find smallest i that satifies this
    while i**digits < 10**(digits-1):
        i += 1
        # i can't be greater than 10 since 10^n has n+1 digits, so if i = 10 here, it's no longer possible
        if i == 10:
            done = True
    # count through i = 9 and increment answer
    while i < 10:
        answer += 1
        i += 1
    if done:
        break
    else:
        digits += 1

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
