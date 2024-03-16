def transcribe(dna):
	return dna.replace('T', 'U')

def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if   nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:           rc.append('N')
	return ''.join(rc)

def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if   codon == 'ATT': aas.append('I')
		elif codon == 'ATC': aas.append('I')
		elif codon == 'ATA': aas.append('I')
		elif codon == 'CTT': aas.append('L')
		elif codon == 'CTC': aas.append('L')
		elif codon == 'CTA': aas.append('L')
		elif codon == 'CTG': aas.append('L')
		elif codon == 'TTA': aas.append('L')
		elif codon == 'TTG': aas.append('L')
		elif codon == 'GTT': aas.append('V')
		elif codon == 'GTC': aas.append('V')
		elif codon == 'GTA': aas.append('V')
		elif codon == 'GTG': aas.append('V')
		elif codon == 'TTT': aas.append('F')
		elif codon == 'TTC': aas.append('F')
		elif codon == 'ATG': aas.append('M')
		elif codon == 'TGT': aas.append('C')
		elif codon == 'TGC': aas.append('C')
		elif codon == 'GCT': aas.append('A')
		elif codon == 'GCC': aas.append('A')
		elif codon == 'GCA': aas.append('A')
		elif codon == 'GCG': aas.append('A')
		elif codon == 'GGT': aas.append('G')
		elif codon == 'GGC': aas.append('G')
		elif codon == 'GGA': aas.append('G')
		elif codon == 'GGG': aas.append('G')
		elif codon == 'CCT': aas.append('P')
		elif codon == 'CCC': aas.append('P')
		elif codon == 'CCA': aas.append('P')
		elif codon == 'CCG': aas.append('P')
		elif codon == 'ACT': aas.append('T')
		elif codon == 'ACC': aas.append('T')
		elif codon == 'ACA': aas.append('T')
		elif codon == 'ACG': aas.append('T')
		elif codon == 'TCT': aas.append('S')
		elif codon == 'TCC': aas.append('S')
		elif codon == 'TCA': aas.append('S')
		elif codon == 'TCG': aas.append('S')
		elif codon == 'AGT': aas.append('S')
		elif codon == 'AGC': aas.append('S')
		elif codon == 'TAT': aas.append('Y')
		elif codon == 'TAC': aas.append('Y')
		elif codon == 'TGG': aas.append('W')
		elif codon == 'CAA': aas.append('Q')
		elif codon == 'CAG': aas.append('Q')
		elif codon == 'AAT': aas.append('N')
		elif codon == 'AAC': aas.append('N')
		elif codon == 'CAT': aas.append('H')
		elif codon == 'CAC': aas.append('H')
		elif codon == 'GAA': aas.append('E')
		elif codon == 'GAG': aas.append('E')
		elif codon == 'GAT': aas.append('D')
		elif codon == 'GAC': aas.append('D')
		elif codon == 'AAA': aas.append('K')
		elif codon == 'AAG': aas.append('K')
		elif codon == 'CGT': aas.append('R')
		elif codon == 'CGC': aas.append('R')
		elif codon == 'CGA': aas.append('R')
		elif codon == 'CGG': aas.append('R')
		elif codon == 'AGA': aas.append('R')
		elif codon == 'AGG': aas.append('R')
		elif codon == 'TAA': aas.append('*')
		elif codon == 'TAG': aas.append('*')
		elif codon == 'TGA': aas.append('*')
		else:                aas.append('X')
	return ''.join(aas)

def gc_comp(seq):
	return(seq.count('C') + seq.count('G')) / len(seq)

def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)

def tm(seq):
	a = 0
	t = 0
	g = 0
	c = 0
	for nt in seq:
		if nt == 'A': a += 1
		if nt == 'T': t += 1
		if nt == 'G': g += 1
		if nt == 'C': c += 1
	if a + t + g + c <= 13: return (a + t) * 2 + (g + c) * 4
	if a + t + g + c >  13: return 64.9 + 41 * (g + c - 16.4) / (a + t + g + c)
