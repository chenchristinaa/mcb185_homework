# 43randomdna.py by Christina Chen

import random

limit = 4
for i in range(1, limit + 1):
	print(f'>seq-{i}')
	randomrange = random.randint(50, 60)
	for j in range(randomrange):
		print(random.choice('ATGC'), end='')
	print()