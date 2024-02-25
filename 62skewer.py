# 62skewer.py by Christina Chen

# python3 62skewer.py ecoli.fa.gz 1000

import sys
import dogma
import mcb185

wsize = int(sys.argv[2]) # size of window

# slow method

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	name = defline.split()
	print(name[0])
	for i in range(0, len(seq) - wsize + 1):
		win = seq[i:i + wsize]
		print(f'{i}\t{dogma.gc_comp(win):.3f}\t{dogma.gc_skew(win):.3f}')

# fast method

alph = 'ABCDEGFHIJKLMNOPQRSTUVWXYZ'
counts = [0] * len(alph)
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	name = defline.split()
	win = seq[0:wsize - 1]
	for pro in win:
		idx = alph.find(pro)
		counts[idx] += 1
	for i in range(wsize, len(seq)):
		if i + wsize > len(seq): continue
		if wsize > len(seq): continue
		idx = alph.find(seq[i])
		counts[idx] += 1
		gc_comp = (counts[2] + counts[5]) / len(seq)
		if counts[2] + counts[5] == 0: gc_skew = 0
		else: gc_skew = (counts[5] - counts[2]) / (counts[2] + counts[5])
		print(f'{name[0]}\t{i}\t{gc_comp:.3f}\t{gc_skew:.3f}')
		inx = alph.find(seq[i - wsize])
		counts[inx] -= 1
