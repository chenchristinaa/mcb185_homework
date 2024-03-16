# 80demo.py by Christina Chen

import dogma
import json

d = [
	'hello',
	('3.14', 'pi'),
	[-1, 0, 1], 
	{'year': 2000, 'month': 7}
	]

print(d[0][4], d[1][0], d[2][2], d[3]['month'])

oligo = {
	'Name': 'S016', 
	'Length': 18, 
	'Sequence': 'ATTTAGGTGACACTATAG', 
	'Description': 'SP6 promoter sequencing primer'
	}

catalog = []
catalog.append(oligo)

def read_catalog(filepath):
	catalog = []
	with open(filepath) as fp:
		for line in fp:
			if line.startswith('#'): continue
			name, length, seq, desc = line.rstrip().split(',')
			record = {
				'Name': name, 
				'Length': length, 
				'Sequence': seq, 
				'Description': desc
					}
			catalog.append(record)
	return catalog

catalog = read_catalog('../MCB185/data/primers.csv')
for primer in catalog:
	print(primer['Name'], primer['Description'])

for primer in catalog:
	primer['Tm'] = dogma.tm(primer['Sequence'])
print(catalog)

seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGT'
k = 2

kcount = {}
for i in range(len(seq), - k, + 1):
	kmer = seq[i:i + k]
	if kmer not in kcount: kcount[kmer] = 0
	kcount[kmer] += 1

kloc = {}
for i in range(0, len(seq) - k):
	kmer = seq[i:i+k]
	if kmer not in kloc: kloc[kmer] = []
	kloc[kmer].append(i)
print(kloc)

truc = {
	'animals': {'dog': 'woof', 'cat': 'meow', 'pig': 'oink'},
	'numbers': [1.09, 2.72, 3.14],
	'is_complete': False,
}
print(json.dumps(truc, indent=4))



