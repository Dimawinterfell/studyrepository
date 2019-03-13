import os

class VirtualBank:

	print('Добро пожаловать в банк "Супер!банк"')
	print('Банк создал Дима, который похитил принцессу')
	print('Год основания банка: сегодня') 
	print('Капитализация банка: что такое капитализация?')


	def registration():
		print('''Для того что бы зарегистрироваться в нашем банке,
введите следующие данные''')

		user = input('Имя аккаунта:')#Задаю переменную 1
		inn = input(str('Введите ваш ИНН:'))# и 2
		balance = 0
		path =  'E:\\Python\\Dpyt\\virtualbankusers\\'  #третья пременная уже задана
		

		if os.path.exists(path+user+'_'+inn):
			print('Такой пользователь уже зарегистрирован')
			saveuser()
		else:
			os.mkdir(path+user+'_'+inn)
			os.chdir(path+user+'_'+inn)
			file = open(user+'_'+inn+'data.txt', 'w')
			file.write('Login:'+str(user)+'\n')
			file.write('INN пользователя:'+inn+'\n')
			file.write('Текущий счёт:'+str(balance))
			file.close()




	def creditwant():
		print('''Вы находитесь кредитном отделе
Для того что бы провести рассчеты, нам необходима следующая информация:''')

		cash = int(input('Сумма кредита>>>'))

		if cash >= 100000 and cash<= 999999:
			print('''Пожалуйста обратитесь в главный банк,
так как такую суммы мы вам выдать не можем,
или введите другую сумму''')
			cashinput()

		elif cash >=1000000 :
			print('А больше вы ничего не хотите?')
			cashinput()
		else:
			return cash

		cash = cashinput()

		percent = int(input('Введите желаемый процент годовых>>>'))

		time = int(input('Введите срок в месяцах>>>'))

		result = cash+(((cash/100)*(percent/12))*time)

		payment = (result / time)

		overpay = (result - cash)

		print('Конечная сумма возврата:',result)
		print('Размер ежемесячного платежа: ',int(payment))
		print('Переплата: ',overpay)





	def acceptfinal():
		acceptcredit = input('Вас устраивает кредит?>>')

		if acceptcredit.lower() == 'да':
			cashpermonth = int(input('Хорошо, введите свой месячный заработок>>>'))
			if cashpermonth > (payment*2) :
				timework = int(input('Хорошо, теперь введите свой опыт работы в годах>>>'))
				if timework >=1  :
					print('Хорошо мы предоставим вам кредит')
				elif timework <1 : 
					print('''К сожалению мы не можем предоставить вам кредит,
так как у вас слишком малый опыт работы''')

			elif cashpermonth < (payment*2) :
				print('''К сожалению мы не сможем вам предоставить кредит,
так как не можем быть уверены что вы его сможете оплатить''')


		if acceptcredit.lower() == 'нет' :
			print('Хорошего вам дня')



registration()
creditwant()
acceptfinal()