# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:09:42 2015

@author: jack.gang
"""

import time  
from EulerFunctions import dijkstra

start = time.clock()

# input text into list of lists
numList = {}
i = 0

f = open('p081_matrix.txt', 'r')
#f = open('p081_test.txt', 'r')
for line in f:
    numList[i] = line.split()
    i += 1
f.close()

# add edges
sourced = False
edges = []
for j in range(0, i):
    lineList = numList[j][0].split(sep=",")
    for k in range(0, len(lineList)):
        if j < i-1:
            edges.append((str(j) + "-" + str(k), str(j+1) + "-" + str(k), int(numList[j+1][0].split(sep=",")[k])))
        if k < i-1:
            edges.append((str(j) + "-" + str(k), str(j) + "-" + str(k+1), int(numList[j][0].split(sep=",")[k+1])))

# find shortest path to bottom
path = dijkstra(edges, "0-0", "79-79")

answer = path[0] + int(numList[0][0].split(sep=",")[0])

elapsed = time.clock() - start
                    
print(str(answer) + " found in " + str(elapsed) + " seconds")
