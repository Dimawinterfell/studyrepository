import os

print('''Здравствуйте!
Вас приветствует Супер!банк
Для того что бы зарегистрироваться в нашем банке,
введите следующие данные''')



def saveuser():

	user = input('Имя аккаунта:')#Задаю переменную 1
	inn = input(str('Введите ваш ИНН:'))# и 2
	balance = 0
	path =  'E:\\Python\\Dpyt\\virtualbankusers\\'  #третья пременная уже задана
	#os.path.exists('D:/Python/Dpyt/virtualbankusers/')

	if os.path.exists(path+user+'_'+inn):
		print('Такой пользователь уже зарегистрирован')
		saveuser()
		# Домашка написать проверку на наличие пути через if:
	else:
		os.mkdir(path+user+'_'+inn)
		os.chdir(path+user+'_'+inn)
		file = open(user+'_'+inn+'data.txt', 'w')
		file.write('Login:'+str(user)+'\n')
		file.write('INN пользователя:'+inn+'\n')
		file.write('Текущий счёт:'+str(balance))
		file.close()

saveuser()