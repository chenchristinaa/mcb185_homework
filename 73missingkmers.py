# 73missingkmers.py by Christina Chen

# python3 73missingkmers.py ecoli.fa.gz 9

import sys
import mcb185
import itertools
import dogma

kcount = {}
totalmissing = 0

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	revseq = dogma.revcomp(seq)
	for k in range(0, 10):

	# counting kmers

		for i in range(0, len(seq)):
			kmer = seq[i:i + k]
			kmee = revseq[i:i + k]
			if kmer not in kcount: kcount[kmer] = 0
			kcount[kmer] += 1			
			if kmee not in kcount: kcount[kmee] = 0
			kcount[kmee] += 1

	# finding missing kmers

		for nts in itertools.product('ACTG', repeat=k):
			kmer = ''.join(nts)
			if kmer not in kcount:
				totalmissing += 1
				print(f'missing kmer: {kmer}')

	# stopping after finding at least one missing kmer

		if totalmissing >= 1: break
