# 50demo.py by Christina Chen

## Indexes
"""
seq = 'GAATTC'
print(seq[0], seq[-1])

for nt in seq:
	print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])
"""
## Slices

s = 'ABCDEFGHIJ'
print(s[0:5])
# 0 is start position
# 5 is end-before position
print(s[0:8:2])
# 2 is step size, default is 1

## Tuples
tax = ('Homo', 'sapiens', 9606)
print(tax)

s[0] = 'C'
tax[0] = 'human'