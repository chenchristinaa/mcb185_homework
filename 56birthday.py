# 56birthday.py by Christina Chen

# python3 56birthday.py 10000 356 23

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

matches = 0
for x in range(trials):
	cal = ['0']
	cal.append(random.randint(1, days + 1))
	for i in range(people):
		d = random.randint(1, days + 1)
		for j in range(len(cal)):
			if d == cal[j]:
				matches +=1
				break
			else:
				cal.append(d)
total = matches / trials
print(total)
