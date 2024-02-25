# coverage

import sys
import random

csize = int(sys.argv[1]) # size of chromosome
rsize = int(sys.argv[2]) # size of read
rnum = int(sys.argv[3]) # number of reads

# create an empty chromosome
chrom = []
for i in range(csize):
	chrom.append(0)

# fill it up with reads
for i in range(rnum):
	pos = random.randint(0, csize - rsize)
	for j in range(rsize):
		chrom[pos + j] += 1
		
print(chrom)

# minimum coverage
min = rnum
for n in chrom[rsize:-rsize]:
	if n < min: min = n
print(min)

# window
k = 15
seq = 'ATCGATCGACTCAGCATCAGCTACGACACTCGAT'
print(seq)
for i in range(0, len(seq) - k + 1, 1):
	win = seq[i:i + k]
	g = win.count('G')
	c = win.count('C')
	print(i, win, (c + g) / len(win))