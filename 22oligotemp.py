# 22oligotemp.py by Christina Chen

def melttemp(a, t, g, c):
	if a + t + g + c <= 13: return (a + t) * 2 + (g + c) * 4
	if a + t + g + c >  13: return 64.9 + 41 * (g + c - 16.4) / (a + t + g + c)

print(melttemp(1, 1, 2, 2))
print(melttemp(1, 2, 3, 4))
print(melttemp(10, 10, 10, 10))
print(melttemp(100, 100, 100, 100))