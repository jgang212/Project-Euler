# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:30:36 2015

@author: jack.gang
"""

import time

def checkIfPalindrome(n):
    number = str(n)
    length = len(number)
    for x in range(0, length / 2):
        if number[x] == number[length - 1 - x]:
            pass
        else:
            return False
    return True

def productPalindrome(largest, smallest):
    a = largest
    b = largest
    currentLargest = 0
    while True:
        check = a * b
        if check < currentLargest or b == smallest:
            if a == smallest:
                break
            a = a - 1
            b = a
            continue
        
        if checkIfPalindrome(check):
            currentLargest = check
        
        b = b - 1
            
    return currentLargest

start = time.time()

answer = productPalindrome(999,100)

elapsed = time.time() - start

print("%s found in %s seconds") % (answer,elapsed)