# 60demo.py by Christina Chen

import mcb185
import sys

# python3 60demo.py ../MCB185/data/A.thaliana.fa.gz
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	A = 0
	C = 0
	G = 0
	T = 0
	N = 0
	nts = 'ACGTN'
	counts = [0] * len(nts)
	for nt in seq:
		idx = nts.find(nt)
		counts[idx] += 1
	print(name, end='\t')
	for n in counts: print(f'{n/len(seq):.4f}', end='\t')
	print()



