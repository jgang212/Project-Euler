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

f = open('p067_triangle.txt', 'r')
for line in f:
    numList[i] = line.split()
    i += 1
f.close()

# add edges
sourced = False
edges = []
for j in range(0, i):
    for k in range(0, len(numList[j])):
        if j < i-1:
        # 100 minus to get shortest path (to find maximum path)
            edges.append((str(j) + str(k), str(j+1) + str(k), 100-int(numList[j+1][k])))
            edges.append((str(j) + str(k), str(j+1) + str(k+1), 100-int(numList[j+1][k+1])))

# find shortest path to bottom
shortestPath = float("inf")
for j in range(0, i):
    endNode = str(i-1) + str(j)    
    path = dijkstra(edges, "00", endNode)
    if path[0] < shortestPath:
        shortestPath = path[0]

answer = 100*(i-1) - shortestPath + int(numList[0][0])

elapsed = time.clock() - start
                    
print(str(answer) + " found in " + str(elapsed) + " seconds")
