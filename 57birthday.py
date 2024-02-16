# 57birthday.py by Christina Chen

# Authors: Christina and Amina

# python3 57birthday.py 10000 365 23

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

matches = 0
for j in range(trials):
	cal = []
	for i in range(days):
		cal.append(0)
	for i in range(people):
		d = random.randint(0, days - 1)
		cal[d] += 1
		if cal[d] > 1:
			matches += 1
			break
total = matches / trials
print(total)