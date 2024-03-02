# 63dust.py by Christina Chen

# python3 63dust.py ecoli.fa.gz 20 1.4

import mcb185
import sys
import math

file  =       sys.argv[1]  # file to be read
wsize =   int(sys.argv[2]) # window size
enlim = float(sys.argv[3]) # entropy threshold

# entropy formula
def shan(a, t, g, c):
	if wsize == 0: sys.exit('Error: Denominator cannot be 0')
	afreq = a / wsize
	tfreq = t / wsize
	gfreq = g / wsize
	cfreq = c / wsize
	if afreq == 0: aexp = 0
	else: aexp  = afreq * math.log2(afreq)
	if tfreq == 0: texp = 0
	else: texp  = tfreq * math.log2(tfreq)
	if gfreq == 0: gexp = 0
	else: gexp  = gfreq * math.log2(gfreq)
	if cfreq == 0: cexp = 0
	else: cexp  = cfreq * math.log2(cfreq)
	entropy = -(aexp + texp + gexp + cexp)
	return entropy
	

for defline, seq in mcb185.read_fasta(file):

	# print first line and converting to list
	
	print(f'>{defline}')
	newseq = list(seq)

	# establish windows and counts
	
	for i in range(0, len(newseq) - wsize):
		window = newseq[i:i + wsize]
		types = 'ATCGN'
		numbs = [0, 0, 0, 0, 0]
		for nt in window:
			idx = types.index(nt)
			numbs[idx] += 1
		a = numbs[0]
		t = numbs[1]
		c = numbs[2]
		g = numbs[3]
		#print(i, a, t, g, c, end=' ')
		ent = shan(a, t, g, c)
		#print(ent)

	# masking
		if ent < enlim: newseq[i:i + wsize] = 'X'
		else: continue
	for i in range(0, len(newseq)):
		if newseq[i] == 'X': newseq[i] = 'N' * wsize
		
	# back to string
	finalseq = ''.join(newseq)
	for i in range(0, len(finalseq), 60):
		print(finalseq[i:i + 60])