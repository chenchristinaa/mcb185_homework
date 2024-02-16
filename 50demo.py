# 50demo.py by Christina Chen

## Indexes

seq = 'GAATTC'
print(seq[0], seq[-1])

for nt in seq:
	print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])

## Slices

s = 'ABCDEFGHIJ'
print(s[0:5])
# 0 is start position
# 5 is end-before position
print(s[0:8:2])
# 2 is step size, default is 1
print(s[::-1])
# prints it in reverse

## Tuples
tax = ('Homo', 'sapiens', 9606)
print(tax)

print(tax[0])
print(tax[::-1])

### Enumerate

# three different ways to do the same thing:

nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])

for i, nt in enumerate(nts):
	print(i, nt)

i = 0
for nt in nts:
	print(i, nt)
	i += 1

### Zip

names = ('adenine', 'cystosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])

for nt, name in zip(nts, names):
	print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

# add stuff to the list with .append()

nts.append('C')
print(nts)

# remove stuff from the end of a list with .pop()

last = nts.pop()
print(last, nts)

# sort lists with .sort() or .sort(reverse=True)

print(nts)
nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nts = ['A', 'T', 'C']
nucleotides = nts
nucleotides.append('C')
print(nts, nucleotides)

items = list() # list() without arguments makes a empty list
print(items)
items.append('eggs')
print(items)

# you can also make empty lists with empty square brackets

stuff = []
print(stuff)

alph = 'ABCDEFGHIJKLMNOPQRSTYVWXYZ'
print(alph)
aas = list(alph)
print(aas)

text = 'good day    to you' # use .split() to turn strings into lists
print(text)
words = text.split()
print(words)

line = '1.41, 2.72, 3.14'
print(line.split(','))
lineline = line.split(',')
print(lineline)

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

if 'A' in alph: print('yay')

alph = 'ABCDEFGHIJKLMNOPQRSTYVXYZ'
print('index G?', alph.index('G'))
#print('index W?', alph.index('W')) # returns an error bc it's not there
print('find G?', alph.find('G'))
print('find W?', alph.find('W')) # returns -1 bc it's not there

#if thing in list: idx = list.index(thing) # for lists/tuples

## Practice Problems

### Minimum value
numbers = ['1', '3', '5', '2', '4']
def minimum(vals):
	mini = vals[0]
	for values in vals[1:]:
		if values < mini: mini = values
	return mini
	
print(minimum(numbers))

## Files

with open(path) as fp:
	for line in fp:
		do_something_with(line)

import gzip
with gzip.open(path, 'rt') as fp:
for line in fp: print(line, end='')













