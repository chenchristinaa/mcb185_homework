# 52entropy.py by Christina Chen

import sys
import math

probs = []
for arg in sys.argv[1:]:
	x = float(arg)
	if x == 0 or x == 1: sys.exit('cannot be 0 or 1')
	probs.append(x)

total = 0
for num in probs:
	total += num
	if not (math.isclose(total, 1)): sys.exit('must sum to 1')

ent = 0
for num in probs:
	ent += -num * math.log2(num)

print(ent)