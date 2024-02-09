# 44randompi.py by Christina Chen

import random

inside = 0
outside = 0
while True:
	x = random.random()
	y = random.random()
	d = ((x ** 2) + (y ** 2)) ** 0.5
	if d < 1: inside  += 1
	else:     outside += 1
	total = inside + outside
	pi = 4 * (inside / total)
	print(pi)
