# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 09:15:11 2015

@author: jack.gang
"""

import pandas
import time

df = pandas.read_csv('11_data.csv', header = None)

def left4Products(x, y, df):
    return df[x][y] * df[x-1][y] * df[x-2][y] * df[x-3][y]
    
def right4Products(x, y, df):
    return df[x][y] * df[x+1][y] * df[x+2][y] * df[x+3][y]
    
def up4Products(x, y, df):
    return df[x][y] * df[x][y-1] * df[x][y-2] * df[x][y-3]
    
def down4Products(x, y, df):
    return df[x][y] * df[x][y+1] * df[x][y+2] * df[x][y+3]
    
def upLeft4Products(x, y, df):
    return df[x][y] * df[x-1][y-1] * df[x-2][y-2] * df[x-3][y-3]
    
def upRight4Products(x, y, df):
    return df[x][y] * df[x+1][y-1] * df[x+2][y-2] * df[x+3][y-3]
    
def downLeft4Products(x, y, df):
    return df[x][y] * df[x-1][y+1] * df[x-2][y+2] * df[x-3][y+3]

def downRight4Products(x, y, df):
    return df[x][y] * df[x+1][y+1] * df[x+2][y+2] * df[x+3][y+3]

start = time.clock()

largestProduct = 0
for x in range(0, len(df[1])):
    for y in range(0, len(df.columns.values)):
        if x >= 3:
            if left4Products(x, y, df) > largestProduct:
                largestProduct = left4Products(x, y, df)
        if x <= len(df[1]) - 4:
            if right4Products(x, y, df) > largestProduct:
                largestProduct = right4Products(x, y, df)
        if y >= 3:
            if up4Products(x, y, df) > largestProduct:
                largestProduct = up4Products(x, y, df)
        if y <= len(df.columns.values) - 4:
            if down4Products(x, y, df) > largestProduct:
                largestProduct = down4Products(x, y, df)
        if x >= 3 and y >= 3:
            if upLeft4Products(x, y, df) > largestProduct:
                largestProduct = upLeft4Products(x, y, df)
        if x >= 3 and y <= len(df.columns.values) - 4:
            if downLeft4Products(x, y, df) > largestProduct:
                largestProduct = downLeft4Products(x, y, df)
        if x <= len(df[1]) - 4 and y >= 3:
            if upRight4Products(x, y, df) > largestProduct:
                largestProduct = upRight4Products(x, y, df)
        if x <= len(df[1]) - 4 and y <= len(df.columns.values) - 4:
            if downRight4Products(x, y, df) > largestProduct:
                largestProduct = downRight4Products(x, y, df)

answer = largestProduct

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))