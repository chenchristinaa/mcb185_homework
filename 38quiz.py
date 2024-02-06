# Authors: Christina, Clarissa

## Task 1

pi = 1
for n in range(3, 10000, 4):
	set = - (1 / n) + (1 / (n + 2))
	pi = pi + set
pi = pi * 4
print(pi)