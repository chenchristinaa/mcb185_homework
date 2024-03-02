# 65transmembrane.py by Christina Chen

# python3 65transmembrane.py ../MCB185/data/GCF_000005845.2_ASM584v2_protein.faa.gz

import sys
import mcb185
import avgkdh

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(0, 22):
		swind = seq[i:i + 8]
		if len(swind) <  8: continue
		if avgkdh.avgkdh(swind) >= 2.5 and 'P' not in swind:
			for j in range(30, len(seq) - 11):
				twind = seq[j:j + 11]
				if len(twind) < 11: continue
				if avgkdh.avgkdh(twind) >= 2.0 and 'P' not in twind:
					print(f'{defline[0:60]}')
					break
			break