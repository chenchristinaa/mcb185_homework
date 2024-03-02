# 25entropy.py by Christina Chen

# Authors: Christina, Lisa, Pearce, Henry

import math
import sys

def shan(a, t, g, c):
	if a + t + g + c == 0: sys.exit('Error: Denominator cannot be 0')
	afreq = a / (a + t + g + c)
	tfreq = t / (a + t + g + c)
	gfreq = g / (a + t + g + c)
	cfreq = c / (a + t + g + c)
	if afreq == 0: sys.exit('Error: Frequency cannot be zero')
	aexp  = afreq * math.log2(afreq)
	if tfreq == 0: sys.exit('Error: Frequency cannot be zero')
	texp  = tfreq * math.log2(tfreq)
	if gfreq == 0: sys.exit('Error: Frequency cannot be zero')
	gexp  = gfreq * math.log2(gfreq)
	if cfreq == 0: sys.exit('Error: Frequency cannot be zero')
	cexp  = cfreq * math.log2(cfreq)
	entropy = -(aexp + texp + gexp + cexp)
	return entropy


print(shan(9, 9, 2, 1))
print(shan(3, 9, 4, 4))
print(shan(4, 4, 1, 1))
print(shan(1, 1, 1, 1))
