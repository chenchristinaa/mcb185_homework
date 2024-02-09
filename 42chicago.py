# 42chicago.py by Christina Chen

import random
import sys

games = 1000000
log = games // 100
totalscore = 0
zeroes = 0
for i in range(games):
	if i % log == 0: print(f'{100 * i/games:.0f}', file=sys.stderr)
	score = 0
	for roundnumber in range(2, 13):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		rolltotal = d1 + d2
		if rolltotal == roundnumber:
#			print(rolltotal, 'yay!')
			score += rolltotal
#		else: print(rolltotal)
#	print(f'total score in round {i}:', score)
#	print(score)
	if score == 0: zeroes += 1
	totalscore += score
	
print(f'average score: {totalscore / games}')
print(f'percentage of zero point games: {(zeroes / games) * 100:.2f}%')