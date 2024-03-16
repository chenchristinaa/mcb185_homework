# 81prosite.py by Christina Chen

# python3 81prosite.py ecoli.protein.gz 

import mcb185
import sys
import re

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if 'DKTGT' in seq: print(defline)


pattern = 'C.{2, 4}C.{3}[LIVMFYWC].{8}H.{3, 5}H'
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if re.search(pattern, seq): print(defline)