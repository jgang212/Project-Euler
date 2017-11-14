# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time    

start = time.clock()

def countCoinWays(coins, total):
    # n+1 rows for the bottom-up table with base case 0 (total = 0)
    table = [[0 for x in range(len(coins))] for x in range(total+1)]
 
    # base case
    for i in range(len(coins)):
        table[0][i] = 1
 
    # fill table bottom up
    for i in range(1, total+1):
        for j in range(len(coins)):
            # solutions including coin[j]
            if i-coins[j] >= 0:
                x = table[i - coins[j]][j]
            else:
                x = 0
 
            # solutions excluding coin[j]
            if j >= 1:
                y = table[i][j-1]
            else:
                y = 0
 
            # total count
            table[i][j] = x + y
 
    return table[total][len(coins)-1]

coins = [1, 2, 5, 10, 20, 50, 100, 200]
total = 200
answer = countCoinWays(coins, total)

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
