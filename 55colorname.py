# 55colorname.py by Christina Chen

# python3 55colorname.py ~/Code/MCB185/data/colors_extended.tsv 200 0 50

import sys
import math

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])
color = R, G, B
color = list(color)

if R > 255 or R < 0: sys.exit('invalid color value, must be between 0 and 255')
if G > 255 or G < 0: sys.exit('invalid color value, must be between 0 and 255')
if B > 255 or B < 0: sys.exit('invalid color value, must be between 0 and 255')

# extract color values
numbers = []
fp = open(colorfile)
for line in fp:
	words = line.split()
	numbers.append(words[2])
fp.close()

# taxi-cab formula
def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d

# minimum formula
def minimum(vals):
	mini = vals[0]
	for values in vals[1:]:
		if values < mini: mini = values
	return mini

# find lowest distance line number
compare = []
linenumber = []
for line in numbers:
	value = line.split(',')
	P = int(value[0]), int(value[1]), int(value[2])
	r = dtc(P, color)
	compare.append(r)
a = compare.index(minimum(compare))

# print Nth line
colors = []
fp = open(colorfile)
for line in fp:
	words = line.split()
	colors.append(words[0])
print(colors[a])