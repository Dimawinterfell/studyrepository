
print('Здравствуйте, Вас приветствует кредитный отдел')

print('Вы обратились с целью взять  кредит')



def cashinput():

	cash = int(input('Итак, введите нужную сумму>>>'))
#	if cash <= 100000:
#		return cash
#	else:
#		print('Это слишком много')
#		cashinput()
	if cash >= 100000 and cash<= 999999:
		print('''Пожалуйста обратитесь в главный банк,
так как такую суммы мы вам выдать не можем,
или введите другую сумму''')
		cashinput()

	elif cash >=1000000 :
		print('Может вам ещё и какао с чаем?')
		cashinput()
	else:
		return cash


cash = cashinput()

percent = int(input('Введите желаемый процент годовых>>>'))

time = int(input('Введите срок в месяцах>>>'))

result = int(cash+(((cash/100)*(percent/12))*time))

payment = (result / time)

overpay = (result - cash)

print('Конечная сумма возврата: ',result)
print('Размер ежемесячного платежа: ',int(payment))
print('Переплата: ',overpay)


acceptcredit = input('Вас устраивает кредит?')

if acceptcredit == 'Да':
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


if acceptcredit == 'Нет' :
	print('Хорошего вам дня')
