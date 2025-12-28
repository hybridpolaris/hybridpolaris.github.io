from time import sleep
from random import randint

bet1 = int(input('place your first bet: '))
bet2 = int(input('place your second bet: '))

finishLine = 197
things = [1] * 4
winners = []
players = [1, 2, 3, 4]

print('|\n' * 4, end = '')

while True:
	print(f'\033[F\033[K\033[F\033[K\033[F\033[K\033[F\033[K1: {" " * (things[0] - 1)}>{" " * (finishLine - things[0])}|\
	2: {" " * (things[1] - 1)}>{" " * (finishLine - things[1])}|\
	3: {" " * (things[2] - 1)}>{" " * (finishLine - things[2])}|\
	4: {" " * (things[3] - 1)}>{" " * (finishLine - things[3])}|', flush = True)

	for i in range(len(players)):
		if things[players[i] - 1] >= finishLine:
			winners.append(players[i])
			players.remove(players[i])
			break
	
	if sum(things) >= finishLine * 4:
		sleep(0.1)
		print(f'Gold: {winners[0]} {"(bet 1)" if winners[0] == bet1 else "(bet 2)" if winners[0] == bet2 else ""}')
		print(f'Silver: {winners[1]} {"(bet 1)" if winners[1] == bet1 else "(bet 2)" if winners[1] == bet2 else ""}')
		print(f'Bronze: {winners[2]} {"(bet 1)" if winners[2] == bet1 else "(bet 2)" if winners[2] == bet2 else ""}')
		print(f'No award: {winners[3]} {"(bet 1)" if winners[3] == bet1 else "(bet 2)" if winners[3] == bet2 else ""}')
		break
	
	sleep(0.1)
	things = [min(thing + randint(0, 2), finishLine) for thing in things]
