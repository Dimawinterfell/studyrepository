def randGame(): 
	import random
	ports = [80,944,255,67]

	print('У тебя есть 4 порта', ports, 'угадай какой из них открытый')
	index = int(input('Введи число от 1 до 4 >>>'))

	if index < 1 or index > 4:
		print('Ты ввел не то что я тебя просил')
		mainGame()
	else:
		winindex = random.randint(0,3)
		index = index - 1

		if index == winindex:
			print('Ты выбрал порт', ports[index])
			print('открытый порт был', ports[winindex])
			print('Ты выиграл!!!')
			mainGame()
		else:
			print('Ты не угадал. Повезет в другой раз')
			print('открытый порт был', ports[winindex])
			mainGame()