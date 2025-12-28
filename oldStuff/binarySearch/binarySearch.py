from random import randint
while 1:
	numberRange = int(input('range: '))
	number: int = randint(1, numberRange)
	choice: int = number - 1
	times: int = 0
	while choice != number:
		times += 1
		choice = int(input(''))
		if choice > number: print('lower')
		elif choice < number: print('higher')
		else: break
	with open(f'scores/{numberRange}.txt', 'a+') as file:
		global average
		file.seek(0)
		file.write(str(times) + '\n')
		data: list = list(map(int, file.readlines()))
		if len(data) == 0: average = times
		else: average = sum(data) / len(data)
		file.close()
	if average > times:
		aboveUnderAverage = 'above average'
	elif average == times:
		aboveUnderAverage = 'average'
	else: 
		aboveUnderAverage = 'under average'
	print('-' * 10)
	print(f'range: {numberRange}\ntries: {times} ({aboveUnderAverage})\naverage: {average}\nanswer: {number}')
	if input('replay (yes/no): ') == 'no': break
