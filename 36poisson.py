# 36poisson.py by Christina Chen

import math

def factorial(x):
	if x == 0: return 1
	a = 1
	for b in range(1, x + 1):
		a = a * b
	return a

def poisson(n, k):
	a = ((n**k * math.e**-n) / factorial(k))
	return a


print(poisson(5, 3))
print(poisson(6, 6))
print(poisson(10, 2))
print(poisson(2, 5))

