from random import randint
from time import sleep

playerTurn: bool = False
items = dealerItems = []
lives = blanks = 0
hearts = dealerHearts = 3
itemDictionary = {

}

while 1:
	if lives + blanks == 0:
		total = randint(2, 10)
		lives = randint(1, total - 1)
		blanks = total - lives
		print(f'reload: \nblanks: {blanks} \nlives: {lives}')
	if playerTurn:
		print('your turn')
		while 1:
			userInput: str = input().split()
			if userInput[0] == 'shoot':
				if randint(lives, blanks + lives) <= lives:
					print('BANG..!')
					if userInput[1] == 'self': hearts -= 1
					elif userInput[1] == 'dealer': dealerHearts -= 1
				else: print('click...')
				break
			elif userInput[0] == 'item':
				if len(items) > 0:
					print('items: ')
					[print(item, end=', ') for item in items[:-1]]
					print(items[-1])
				else: print('no items')
	else:
		print('computer turn')

	playerTurn = not playerTurn
	sleep(0.1)