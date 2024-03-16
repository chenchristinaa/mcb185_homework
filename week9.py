# Lists in Lists

matrix = [
[1, 2, 3],
[4, 5, 6, 7, [7.5, 7.75]],
[8, 9]
]

print(matrix)          # [[1, 2, 3], [4, 5, 6, 7, [7.5, 7.75]], [8, 9]]
print(matrix[2][1])    # 9
print(matrix[1][4][1]) # [7.5, 7.75]
print(matrix[1][4][1]) # 7.75

# Another One

person = {
	'name': 'Christina Chen',
	'age': 21,
	'married': False,
	'mentees': {
		'Claire': 'undergrad',
		'Dell': 'undergrad'
		}
}

print(person)                      # {'name': 'Christina Chen', 'age': 21, 'married': False, 'mentees': {'Claire': 'undergrad', 'Dell': 'undergrad'}}
print(person['mentees'])           # {'Claire': 'undergrad', 'Dell': 'undergrad'}
print(person['mentees']['Claire']) # undergrad

people = []
print(people)
people.append(person)
print(people)
people[0]['making a new category'] = 'hi there'
people[0]['mentees'].append('Isla')
print(people)

# Programs with Matrices

import json
import sys
import mcb185

## python3 ../MCB185/data/C.elegans.fa.gz 2

k = int(sys.argv[2])
kloc = {}
for defline, seq in mcb185_read.fasta(sys.argv[1]):
	words = defline.split()
	chrom = words[0]
	for i in range(len(seq) - k + 1):
		kmer = seq[i:i + k]
		if kmer not in kloc: klock[kmer] = []
		if chrom not in kloc[kmer]: kloc[kmer][chrom] = []
#		kloc[kmer].append( (chrom, i) )
		kloc[kmer][chrom].append[i]

print(json.dumps(kloc, indent=4))