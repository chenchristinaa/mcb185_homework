# 71countgff.py by Christina Chen

# python3 71countgff.py ecoli.gff.gz | sort				sort results
# python3 71countgff.py ecoli.gff.gz | sort -n			ascending by first column
# python3 71countgff.py ecoli.gff.gz | sort -nk2	    ascending by second column
# python3 71countgff.py ecoli.gff.gz | sort -rnk2		descending by second column


import gzip
import sys

count = {}
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line.startswith('#'): continue
		f = line.split()
		feature = f[2]
		if feature not in count: count[feature] = 0
		count[feature] += 1
for f, n, in count.items(): print(f, n)

# sorting inside python

for k in sorted(count): print(k, count[k]) # ascending by first column

for k, v in sorted(count.items(), key=lambda item: item[1]):
	print(k, v) # ascending by second column

# another method

def by_value(tuple):
	return tuple[1]

for k, v in sorted(count.items(), key=by_value):
	print(k, v)