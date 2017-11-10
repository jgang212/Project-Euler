# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:18:07 2017

@author: jack.gang
"""

import time
from EulerFunctions import isPrime

start = time.time()

def findM(p, q, N):
    checkN = N - N % (p*q)  # has to be divisible by p and q
    
    while True:
        divided = checkN
        while divided % q == 0:
            divided /= q
        while divided % p == 0:
            divided /= p
        if divided == 1:
            return checkN
        else:
            checkN -= p*q            

N = 10000000
primeList = []
for i in range(2, N//2):    # only care up to N/2 since smallest prime is 2
    if isPrime(i):
        primeList.append(i)

answer = 0
for i in range(0, len(primeList)):
    for j in range(i+1, len(primeList)):
        if primeList[i] * primeList[j] > N:
            break
        answer += findM(primeList[i], primeList[j], N)

elapsed = time.time() - start

print("{} found in {} seconds".format(answer,elapsed))