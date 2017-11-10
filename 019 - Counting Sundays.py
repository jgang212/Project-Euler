# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 11:52:31 2015

@author: jack.gang
"""

import time    

start = time.clock()

days = 365
count = 0
for year in range(1,101):
    for month in range(1,13):
        if days % 7 == 6:
            count = count + 1
            
        monthDays = 0
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            monthDays = 31
        if month == 2:
            if year % 4 == 0:
                monthDays = 29
            else:
                monthDays = 28
        if month == 4 or month == 6 or month == 9 or month == 11:
            monthDays = 30
        days = days + monthDays

answer = count

elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))