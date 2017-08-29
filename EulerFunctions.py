# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 10:07:47 2017

@author: jack.gang
"""

import math
from collections import defaultdict
from heapq import heappop, heappush

def isPrime(n):
    # trivial cases
    if n <= 1:
        return False
    if n in [2, 3, 5]:
        return True
    if n % 2 == 0:
        return False
    
    # divisibility rules
    # 3
    digitSum = 0
    for digit in str(n):
        digitSum += int(digit)
    if digitSum % 3 == 0:
        return False
    # 5
    if str(n)[-1:] in [0, 5]:
        return False
    
    # hard check
    limit = int(n**0.5)
    for x in range(2, limit+1):
        if n % x == 0:
            return False
    return True

def countDivisors(n):
    count = 0
    limit = int(math.floor(n**0.5))
    for x in range(1, limit+1):
        if n % x == 0:
            count = count + 1
    count = count * 2
    if float(n**0.5).is_integer():
        count = count - 1
    return count

def sumOfDigits(n):
    str_n = str(n)
    totalSum = 0
    for x in range(0, len(str_n)):
        totalSum = totalSum + int(str_n[x])
    return totalSum

# djikstra's shortest paths
def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen = [(0,f,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))

    return float("inf")

def findDivisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n))+1):
        if (n % i == 0):
            divisors.append(i)
            if (i != 1) and (int(n / i) not in divisors):
                divisors.append(int(n / i))
    return sorted(divisors)

def convertToBinary(n):
    binaryStr = ""
    while n > 0:
        if n % 2 == 0:
            binaryStr = "0" + binaryStr            
        else:
            binaryStr = "1" + binaryStr
        n = n // 2
    return binaryStr

def checkIfPalindrome(n):
    number = str(n)
    length = len(number)
    for x in range(0, length // 2):
        if number[x] == number[length - 1 - x]:
            pass
        else:
            return False
    return True

def isPandigital(n):
    for i in range(1, len(str(n))+1):
        if str(i) not in str(n):
            return False
    return True

def findPrimeFactors(n, primeList):
    result = []
    if n in primeList:
        result.append(n)
    for prime in primeList:
        if prime > n:
            break
        if n % prime == 0:
            result.append(prime)
    return result

def round_down(n, divisor):
    return n - (n % divisor)