# 37nilakantha.py by Christina Chen

pi = 3
for n in range(2, 100000, 4):
	mid = (4 / (n * (n + 1) * (n + 2)))
	end = (4 / ((n + 2) * (n + 3) * (n + 4)))
	pi = pi + mid - end
print(pi)