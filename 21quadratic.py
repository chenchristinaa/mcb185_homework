# 21quadratic.py by Christina Chen

# Authors: Christina Chen, Yutong, Ian

import math
import sys

def quadratic(a, b, c):
	if a == 0: sys.exit('Error: Denominator cannot be zero')
	if b**2 - 4 * a * c < 0: sys.exit('Error: Cannot square root negative number')
	x1 = (-1 * b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
	x2 = (-1 * b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
	return x1, x2

print(quadratic(1, 5, 1))
print(quadratic(1, -5, 1))
print(quadratic(-1, 1, 1))
print(quadratic(0.5, -5, 1))
print(quadratic(0, -5, 1))