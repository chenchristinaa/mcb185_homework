# 47deathsaves.py by Christina Chen

import random

statroll = 10000000

success = 0
failure = 0
death = 0
revive = 0
stable = 0
totalrolls = 0

for i in range(statroll):
	r1 = random.randint(1, 20)
	if r1 == 1:
		failure += 2
		if failure >= 3:
			death += 1
			failure = 0
			totalrolls += 1
	elif r1 == 20:
		revive += 1
		totalrolls += 1
	elif r1 >= 10:
		success += 1
		if success >= 3:
			stable += 1
			success = 0
			totalrolls += 1
	elif r1 < 10:
		failure += 1
		if failure >= 3:
			death += 1
			failure = 0
			totalrolls += 1
			
print(f'death:\t{death / totalrolls}')
print(f'stable:\t{stable  / totalrolls}')
print(f'revive:\t{revive  / totalrolls}')