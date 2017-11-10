# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:24:57 2015

@author: jack.gang
"""

import time
from EulerFunctions import shoelacePolygonArea
    
start = time.time()

def findQuadrant(coordinates):
    if coordinates[0] > 0 and coordinates[1] > 0:
        return 1
    elif coordinates[0] < 0 and coordinates[1] < 0:
        return 3
    elif coordinates[0] < 0 and coordinates[1] > 0:
        return 2
    elif coordinates[0] > 0 and coordinates[1] < 0:
        return 4
    else:
        return 0

# input text into list of lists
triangleList = []

f = open('p102_triangles.txt', 'r')
for line in f:
    triangleList.append(line.split(sep=","))
f.close()

adjacentQuadrantSets = [{1, 2}, {2, 3}, {3, 4}, {1, 4}]
oppositeQuadrantSets = [{1, 3}, {2, 4}]
answer = 0
for triangle in triangleList:
    X1 = int(triangle[0])
    Y1 = int(triangle[1])
    X2 = int(triangle[2])
    Y2 = int(triangle[3])
    X3 = int(triangle[4])
    Y3 = int(triangle[5])
    
    # can't all be in same quadrant
    if findQuadrant([X1,Y1]) == findQuadrant([X2,Y2]) == findQuadrant([X3,Y3]):
        continue
    # can't be all in adjacent quadrants
    quadrantList = set([findQuadrant([X1,Y1]), findQuadrant([X2,Y2]), findQuadrant([X3,Y3])])
    if quadrantList in adjacentQuadrantSets:
        continue
    
    area1 = shoelacePolygonArea([[X1,Y1], [X2,Y2], [0,0]])
    area2 = shoelacePolygonArea([[X1,Y1], [X3,Y3], [0,0]])
    area3 = shoelacePolygonArea([[X3,Y3], [X2,Y2], [0,0]])
    totalArea = shoelacePolygonArea([[X1,Y1], [X2,Y2], [X3,Y3]])
    if totalArea == (area1 + area2 + area3):      
        answer += 1

elapsed = time.time() - start

print("{} found in {} seconds".format(answer,elapsed))
 