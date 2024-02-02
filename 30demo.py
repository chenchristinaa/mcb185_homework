# 30demo.py by Christina Chen

## Iteration

i = 0
while True:
	i = i + 1
	print('hey', i)
	if i == 3: break
	
i = 0
while i < 3:
	print(i)
	i = i + 1
print('final value of i is', i)

i = 0
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)

for i in range(1, 10, 3):
# starting value, stop before next value, increase by value
	print(i)

for i in range(0, 5):
	print(i)

for i in range(5):
	print(i)

for char in 'hello':
	print(char)

seq = 'GAATTC'
for nt in seq:
	print(nt)

nts = 'ACGT'
for nt1 in nts:
	for nt2 in nts:
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:          print(nt1, nt2, '-1')

i = 0
limit = 4
for i in range(0, limit):
	for j in range(i + 1, limit):
		print(i + 1, j + 1)

def gc_comp(seq):
	gc_count = 0
	total = 0
	for nt in seq:
		if nt == 'C' or nt == 'G':
			gc_count = gc_count + 1
		total = total + 1
	return gc_count / total

print(gc_comp('ACAGCGAAT'))

### Practice

#### Triangular Number

def tri(x):
	i = 0
	for n in range(1, x+1):
		a = i + n
	return a
	
print(tri(3))

#### Factorial

def factorial(x):
	if x == 0: return 1
	a = 1
	for b in range(1, x + 1):
		a = a * b
	return a

print(factorial(3))