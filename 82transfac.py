# 82transfac.py by Christina Chen

# python3 82transfac.py ../MCB185/data/*.transfac.gz

import json
import sys
import gzip


"""
with gzip.open(sys.argv[1], 'rt') as fp:
    catalog = {}
    for line in fp:
        words = line.split()
        if line.startswith('ID'): catalog[id] = words[1]
print(catalog)


"""
with gzip.open(sys.argv[1], 'rt') as fp:
	catalog = []
	catalog.append('id')
	catalog.append('pwd')
	print(catalog)
	for line in fp:
		words = line.split()
		if line.startswith('ID'): catalog['id'].append(words[1])
		if line.startswith('0') or line.startswith('1'):
			record = {
			'A': words[1],
			'C': words[2],
			'G': words[3],
			'T': words[4]
			} 
		catalog['pwd'].append(record)
print(catalog)
"""

def read_transfac(filepath):
	transfac = []
	with open(filepath) as fp:
		for line in fp:
			if line.startswith('ID'): ids = line[1]
			if line.startswith('0'): a = line[1]
			if line.startswith('0'): c = line[2]
			if line.startswith('0'): g = line[3]
			if line.startswith('0'): t = line[4]
			record = {
				'id': ids,
				'pwm': {
					'A': a,
					'C': c,
					'G': g,
					'T': t
				}
			}
			catalog.append(record)
	return catalog

catalog = read_transfac(sys.argv[1])

print(catalog)


catalog = {
			'id': [],
			'pwm': {
				'A': [],
				'C': [],
				'G': [],
				'T': []
			}
}

fp = open(sys.argv[1])
for line in fp:
	print(line)
	#words = line.split()
	#if line.startswith('ID'): catalog['id'].append = words[1]
fp.close()

print(catalog)

final = []
def read_transfac(filepath):
	catalog = {'id': {},
				'pwm': []}
	with gzip.open(filepath, 'rt') as fp:
		for line in fp:
			words = line.split()
			if line.startswith('ID'):
				catalog[0]['id'] = words[1]
			if line.startswith('0') or line.startswith('1'):
					catalog['pwm'].append(('A','C', 'G', 'T'))
					
			final.append(catalog)
	return final

final = read_transfac(sys.argv[1])
print(json.dumps(final, indent=4))
"""