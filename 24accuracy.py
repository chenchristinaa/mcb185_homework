# 24accuracy.py by Christina Chen

# Authors: Christina, Lisa

import sys

"""
tp is true positive
fp false positive
tn is true negative
fn is false positive
"""

def stats(tp, fp, tn, fn):
	if tp + fp + tn + fn == 0: sys.exit('Error: Denominator cannot be 0')
	accuracy = (tp + tn) / (tp + fp + tn + fn)
	if tp + fp == 0: sys.exit('Error: Denominator cannot be 0')
	precision = tp / (tp + fp)
	if tp + fn == 0: sys.exit('Error: Denominator cannot be 0')
	recall = tp / (tp + fn)
	if precision + recall == 0: sys.exit('Error: Denominator cannot be 0')
	f1 = 2 * (precision * recall) / (precision + recall)
	return accuracy, f1

print(stats(100, 20, 200, 25))
print(stats(50, 5, 10, 1000))
print(stats(5, 5, 5, 5))
print(stats(0, 0, 0, 0))
