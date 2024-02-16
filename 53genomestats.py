# 53genomestats.py by Christina Chen

# python3 53genomestats.py ~/Code/MCB185/data/A.thaliana.gff.gz gene

import gzip
import sys
import math

path = sys.argv[1]
feature = sys.argv[2]

lengths = []
with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		words = line.split()
		if words[2] == feature:
			beginning = int(words[3])
			ending = int(words[4])
			length = ending - beginning + 1
			lengths.append(length)

# count
print('count:', len(lengths))

# min
lengths.sort()
print('minimum:', lengths[0])

# max
print('maximum:', lengths[-1])

# mean
total = 0
for num in lengths:
	total += num
	mean = total / len(lengths)
print('mean:', mean)

# standard deviation
a = 0
for num in lengths:
	a += (num - mean) ** 2
sd = math.sqrt(a / len(lengths))
print('standard deviation:', sd)

# median
i = len(lengths) / 2
if i % 1 == 0:
	i = int(i)
	f = int(i + 1)
	median = (lengths[i] + lengths[f]) / 2
	print('medians:', median)
else:
	f = int(i + 0.5)
	print('median:', lengths[f])



