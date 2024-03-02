# 23hydropathy.py by Christina Chen

import sys

def kdhydro(x):
	if x == 'A': return  1.80
	if x == 'C': return  2.50
	if x == 'D': return -3.50
	if x == 'E': return -3.50
	if x == 'F': return  2.80
	if x == 'G': return -0.40
	if x == 'H': return -3.20
	if x == 'I': return  4.50
	if x == 'K': return -3.90
	if x == 'L': return  3.80
	if x == 'M': return  1.90
	if x == 'N': return -3.50
	if x == 'P': return -1.60
	if x == 'Q': return -3.50
	if x == 'R': return -4.50
	if x == 'S': return -0.80
	if x == 'T': return -0.70
	if x == 'V': return  4.20
	if x == 'W': return -0.90
	if x == 'Y': return -1.30
	else:        sys.exit('Error: Not an amino acid')
	
print(kdhydro('A'))
print(kdhydro('C'))
print(kdhydro('R'))
print(kdhydro('Z'))