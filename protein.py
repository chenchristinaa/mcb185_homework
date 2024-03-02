import random
import sys

# kdh equation
def kdh(x):
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
	return 0
	
# make a random protein
length = 100
protein = []
prots = 'ACDEFGHIKLMNPQRSTVWXY'
for i in range(0, length):
	aa = random.choice(prots)
	protein.append(aa)
	seq = ''.join(protein)
print(protein)

# average kdh
sumkdh = 0
for prot in seq:
	sumkdh += kdh(prot)
print(sumkdh/length)

# different way to do it
def avgkdh(x):
	kdh = 0
	if x == 'A': kdh +=  1.80
	if x == 'C': kdh +=  2.50
	if x == 'D': kdh += -3.50
	if x == 'E': kdh += -3.50
	if x == 'F': kdh +=  2.80
	if x == 'G': kdh += -0.40
	if x == 'H': kdh += -3.20
	if x == 'I': kdh +=  4.50
	if x == 'K': kdh += -3.90
	if x == 'L': kdh +=  3.80
	if x == 'M': kdh +=  1.90
	if x == 'N': kdh += -3.50
	if x == 'P': kdh += -1.60
	if x == 'Q': kdh += -3.50
	if x == 'R': kdh += -4.50
	if x == 'S': kdh += -0.80
	if x == 'T': kdh += -0.70
	if x == 'V': kdh +=  4.20
	if x == 'W': kdh += -0.90
	if x == 'Y': kdh += -1.30
	kdh += 0

# another way to do it
AAS = 'ACDEFGHIKLMNPQRSTVWXY'
KDH = (1.80, 2.50, -3.50, -3.50, 2.80, -0.40, -3.20, 4.50, 
		-3.90, 3.80, 1.90, -3.50, -1.60, -3.50, -4.50, 
		-0.80, -0.70, 4.20, -0.90, -1.30, 0)
kdhs = 0
for prot in seq:
	idx = AAS.index(prot)
	kdhs += KDH[idx]
print(kdhs / length)