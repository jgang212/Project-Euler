import numpy as np

def isPrime(n):
	for i in range(2, int(np.floor(np.sqrt(n)))+1):
		if n % i == 0:
			return False
	return True

maxN = 0
maxA = 0
maxB = 0
for a in range(-999, 1000):
	for b in range(2, 1001):		# b has to be positive and prime
		if isPrime(b):
			n = 1
			while(True):
				res = n**2 + a*n + b
				if res < 2 or not isPrime(res):
					if n > maxN:
						maxN = n
						maxA = a
						maxB = b
					break
				else:
					n = n + 1

print("result", maxN, maxA, maxB)