# 46savingthrows.py by Christina Chen

import random

statroll = 10000000

d5success = 0
d10success = 0
d15success = 0
totalrolls = 0

print('DC:\t5\t10\t15')

## Normal

for i in range(statroll):
	r1 = random.randint(1, 20)
	totalrolls += 1
	if r1 >=  5: d5success += 1
	if r1 >= 10: d10success += 1
	if r1 >= 15: d15success += 1
print('norm:', end='\t')
print(f'{d5success  / totalrolls:.3f}', end='\t')
print(f'{d10success / totalrolls:.3f}', end='\t')
print(f'{d15success / totalrolls:.3f}', end='\t')
print()

### Advantaged

d5success = 0
d10success = 0
d15success = 0
totalrolls = 0

for i in range(statroll):
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	totalrolls += 1
	if r1 > r2:
		if r1 >=  5: d5success += 1
		if r1 >= 10: d10success += 1
		if r1 >= 15: d15success += 1
	else:
		if r2 >=  5: d5success += 1
		if r2 >= 10: d10success += 1
		if r2 >= 15: d15success += 1
	

print('adv:', end='\t')
print(f'{d5success  / totalrolls:.3f}', end='\t')
print(f'{d10success / totalrolls:.3f}', end='\t')
print(f'{d15success / totalrolls:.3f}', end='\t')
print()

### Disadvantaged

d5success = 0
d10success = 0
d15success = 0
totalrolls = 0

for i in range(statroll):
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	totalrolls += 1
	if r1 < r2:
		if r1 >=  5: d5success += 1
		if r1 >= 10: d10success += 1
		if r1 >= 15: d15success += 1
	else:
		if r2 >=  5: d5success += 1
		if r2 >= 10: d10success += 1
		if r2 >= 15: d15success += 1
	

print('dis:', end='\t')
print(f'{d5success  / totalrolls:.3f}', end='\t')
print(f'{d10success / totalrolls:.3f}', end='\t')
print(f'{d15success / totalrolls:.3f}', end='\t')
print()