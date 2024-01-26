# 23hydropathy.py by Christina Chen

import sys

def kdhydro(x):
	if x == 'a': return  1.80
	if x == 'c': return  2.50
	if x == 'd': return -3.50
	if x == 'e': return -3.50
	if x == 'f': return  2.80
	if x == 'g': return -0.40
	if x == 'h': return -3.20
	if x == 'i': return  4.50
	if x == 'k': return -3.90
	if x == 'l': return  3.80
	if x == 'm': return  1.90
	if x == 'n': return -3.50
	if x == 'p': return -1.60
	if x == 'q': return -3.50
	if x == 'r': return -4.50
	if x == 's': return -0.80
	if x == 't': return -0.70
	if x == 'v': return  4.20
	if x == 'w': return -0.90
	if x == 'y': return -1.30
	else:        sys.exit('Error: Not an amino acid')
	
print(kdhydro('a'))
print(kdhydro('c'))
print(kdhydro('r'))
print(kdhydro('z'))