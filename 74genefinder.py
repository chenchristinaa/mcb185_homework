# 74genefinder.py by Christina Chen

# Authors: Christina Chen, Ian Korf, Amina

# python3 74genefinder.py ecoli.fa.gz 300 | sort -n -k 4

import mcb185
import sys
import dogma

# finding frames

def frames(gene, msize):
	stops = ('TAG', 'TAA', 'TGA')
	keep = []
	
	for i in range(0, 3):
		seq = gene[i:]
		place = 0
		
	# start codon

		while place < len(seq):			
			if seq[place:place + 3] != 'ATG':
				place += 3
				continue
			
	# stop codon
			
			for j in range(place, len(seq), 3):
				codon = seq[j:j + 3]
				if codon in stops: break
			
	# keep the middle bits
			
			length = j - place + 1
			if length > msize:
				coords = (place, j)
				keep.append(coords)
	
	# continue to next frame
	
			place = j
			
	# finish
	
	return keep

# main function

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	words = defline.split()
	revseq = dogma.revcomp(seq)

	# forward strand
	
	for start, end in frames(seq, int(sys.argv[2])):
		print(f'{words[0]}\tRefSeq\tCDS\t{start}\t{end}\t.\t+\t0\tID=cds')
	
	# reverse strand
	
	for start, end in frames(revseq, int(sys.argv[2])):
		place = len(seq) - end  - 2
		stop = len(seq) - begin
		print(f'{words[0]}\tRefSeq\tCDS\t{start}\t{end}\t.\t-\t0\tID=cds')