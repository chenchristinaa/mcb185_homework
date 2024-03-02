def avgkdh(seq):
	total = 0
	for x in seq:
		if x == 'A': total +=  1.80
		if x == 'C': total +=  2.50
		if x == 'D': total += -3.50
		if x == 'E': total += -3.50
		if x == 'F': total +=  2.80
		if x == 'G': total += -0.40
		if x == 'H': total += -3.20
		if x == 'I': total +=  4.50
		if x == 'K': total += -3.90
		if x == 'L': total +=  3.80
		if x == 'M': total +=  1.90
		if x == 'N': total += -3.50
		if x == 'P': total += -1.60
		if x == 'Q': total += -3.50
		if x == 'R': total += -4.50
		if x == 'S': total += -0.80
		if x == 'T': total += -0.70
		if x == 'V': total +=  4.20
		if x == 'W': total += -0.90
		if x == 'Y': total += -1.30
		else:        total +=  0
	average = total / len(seq)
	return average