# 45dndstats.py by Christina Chen

import random
import sys

statrolls = 10000000

## 3D6: roll 3 six-sided dice

rolls = 0
totalstat = 0
for j in range(statrolls):
	r1 = random.randint(1, 6)
	r2 = random.randint(1, 6)
	r3 = random.randint(1, 6)
	total = r1 + r2 + r3
	rolls += 1
	totalstat += total
print(f'3D6:\naverage stat: {totalstat / rolls}')

## 3D6r1: roll 3 six-sided dice, but re-roll any 1s

rolls = 0
totalstat = 0
for j in range(statrolls):
	r1 = random.randint(1, 6)
	r2 = random.randint(1, 6)
	r3 = random.randint(1, 6)
	while r1 == 1:
		r1 = random.randint(1, 6)
	while r2 == 1:
		r2 = random.randint(1, 6)
	while r3 == 1:
		r3 = random.randint(1, 6)
	total = r1 + r2 + r3
	rolls += 1
	totalstat += total
print(f'3D6r1:\naverage stat: {totalstat / rolls}')

## 3D6x2: roll pairs of six-sided 3 times, taking the maximum each time

rolls = 0
total = 0
totalstat = 0
for j in range(statrolls):
	for i in range(3):
		r1 = random.randint(1, 6)
		r2 = random.randint(1, 6)
		if r1 > r2: total += r1
		else:       total += r2
	rolls += 1
totalstat += total
print(f'3D6x2:\naverage stat: {totalstat / rolls}')

## 4D6d1: roll 4 six-sided dice, dropping the lowest die roll

rolls = 0
totalstat = 0
total = 0

for j in range(statrolls):
	r1 = random.randint(1, 6)
	r2 = random.randint(1, 6)
	r3 = random.randint(1, 6)
	r4 = random.randint(1, 6)
	if r1 <= r2 and r1 <= r3 and r1 <= r4:
		total = r2 + r3 + r4
	if r2 <= r1 and r2 <= r3 and r2 <= r4:
		total = r1 + r3 + r4
	if r3 <= r1 and r3 <= r2 and r3 <= r4:
		total = r1 + r2 + r4
	if r4 <= r1 and r4 <= r2 and r4 <= r3:
		total = r1 + r2 + r3
rolls += 1
totalstat += total
print(f'4D6d1:\naverage stat: {totalstat / rolls}')
