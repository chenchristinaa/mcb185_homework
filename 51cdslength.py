# 51cdslength.py by Christina Chen

import gzip

lengths = []
path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		words = line.split()
		if words[2] == 'CDS': continue
		beginning = int(words[3])
		ending = int(words[4])
		length = ending - beginning + 1
		lengths.append(length)