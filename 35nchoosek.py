#35nchoosek.py by Christina Chen

import sys

def factorial(x):
	if x == 0: return 1
	a = 1
	for b in range(1, x + 1):
		a = a * b
	return a

def nchoosek(n, k):
	if n < k: sys.exit('Error, n must be greater than k')
	else:     c = factorial(n) / (factorial(k) * factorial(n - k))
	return c

print(nchoosek(13, 2))
print(nchoosek(25, 6))
print(nchoosek(34, 1))
print(nchoosek(3, 4))
