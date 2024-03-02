# 62skewer.py by Christina Chen

# python3 62skewer.py ecoli.fa.gz 1000

import sys
import dogma
import mcb185

file  =     sys.argv[1]  # file to be read
wsize = int(sys.argv[2]) # size of window

# slow method

for defline, seq in mcb185.read_fasta(file):
	for i in range(0, len(seq) - wsize):
		window = seq[i:i + wsize]
		comp = dogma.gc_comp(window)
		skew = dogma.gc_skew(window)
		#print(f'{comp:.3f}\t{skew:.3f}')

# fast method

for defline, seq in mcb185.read_fasta(file):

	# starting window
	
	initialwindow = seq[0:wsize]
	#print(initialwindow)
	types = 'ATCG'
	numbs = []
	for nt in types:
		numbs.append(0)
	#print(numbs)
	for nt in initialwindow:
		idx = types.index(nt)
		numbs[idx] += 1
		#print(nt, numbs)
	#print(numbs)
	comp = (numbs[2] + numbs[3]) / wsize
	skew = (numbs[3] - numbs[2]) / (numbs[3] + numbs[2])
	#print(f'comp:\tskew:')
	#print(f'{comp:.3f}\t{skew:.3f}')

	# removing an nt and adding an nt
	
	for i in range(0, len(seq) - wsize):
		idx = types.index(seq[i])
		numbs[idx] -= 1
		inx = types.index(seq[i + wsize])
		numbs[inx] += 1
		#print(seq[i], numbs, seq[i + wsize])
		comp = (numbs[2] + numbs[3]) / wsize
		if numbs[3] + numbs[2] == 0: skew = 0
		else: skew = (numbs[3] - numbs[2]) / (numbs[3] + numbs[2])
		#print(f'{comp:.3f}\t{skew:.3f}')