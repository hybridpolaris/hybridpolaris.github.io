from random import randint


while 1:
	chambers: int = 0
	while chambers <= 0:
		chambers = int(input('total chambers: '))

	newChambers: int = chambers
	rounds: int = 0
	while randint(1, newChambers) != 1:
		print(f'click... ({round(1 / newChambers * 100, 2)}%)', end='')
		newChambers -= 1
		rounds += 1
		input()
	
	print(f'BANG..! ({round(1 / newChambers * 100, 2)}%) \n')
	print('-' * 10)

	with open(f'scores/{chambers}', 'a+') as file:
		global average
		file.seek(0)
		file.write(str(rounds) + '\n')
		data: list = list(map(int, file.readlines()))
		if len(data) == 0: average = rounds
		else: average = sum(data) / len(data)
		file.close()
	if average > rounds:
		aboveUnderAverage = 'worse than average'
	elif average < rounds:
		aboveUnderAverage = 'better than average'
	else: 
		aboveUnderAverage = 'average'

	print(f'chambers: {chambers} \nrounds survived: {rounds} \n{aboveUnderAverage} ({round(average, 2)})')
	if input('replay (yes/no): ') == 'no': break
	print('')
