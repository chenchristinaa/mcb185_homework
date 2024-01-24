# 24accuracy.py by Christina Chen

"""
tp is true positive
fp false positive
tn is true negative
fn is false positive
"""

def stats(tp, fp, tn, fn):
	accuracy = (tp + tn) / (tp + fp + tn + fn)
	precision = tp / (tp + fp)
	recall = tp / (tp + fn)
	f1 = 2 * (precision * recall) / (precision + recall)
	print(accuracy, f1)

stats(100, 20, 200, 25)
stats(1, 2000, 200, 25)
stats(50, 5, 10, 1000)
stats(5, 5, 5, 5)
