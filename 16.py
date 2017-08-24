# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:58:33 2015

@author: jack.gang
"""

import time
from EulerFunctions import sumOfDigits

start = time.time()

answer = sumOfDigits(2**1000)

elapsed = time.time() - start

print("{} found in {} seconds".format(answer,elapsed))