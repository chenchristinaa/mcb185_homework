# 70demo.py by Christina Chen

# making a dictionary

d = {'dog': 'woof', 'cat': 'meow'}
print(d)                       # {'dog': 'woof', 'cat': 'meow'}
print(d['cat'])                # meow
if 'dog' in d: print(d['dog']) # woof
if 'rat' in d: print(d['rat']) # (prints nothing)

# adding to dictionary

d['pig'] = 'oink'
print(d) # {'dog': 'woof', 'cat': 'meow', 'pig': 'oink'}

# changing in the dictionary

d['cat'] = 'mew'
print(d) # {'dog': 'woof', 'cat': 'mew', 'pig': 'oink'}

# iteration with dictionaries

for key in d: print(f'{key} says {d[key]}')
	# dog says woof
	# cat says mew
	# pig says oink

for k, v in d.items(): print(k, 'says', v)
	# dog says woof
	# cat says mew
	# pig says oink

print(d.keys(), d.values(), list(d.values()))

# using intertools

import itertools
for nts in itertools.product('ACGT', repeat=2):
	print(nts)