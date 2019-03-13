

from datetime import datetime, timedelta


def rename_current_day_to_russian():
	now = datetime.now()
	day = now.strftime('%A')
	if day == 'Sunday':
		print('Сегодня Воскресенье')
	elif day == 'Monday':
		print('Сегодня Понедельник')
	elif day == 'Tuesday':
		print('Сегодня Вторник ')
	elif day == 'Wednesday':
		print('Сегодня Среда')
	elif day == 'Thursday':
		print('Сегодня Четверг')
	elif day == 'Friday':
		print('Сегодня Пятница')
	elif day == 'Saturday':
		print('Сегодня Суббота')
	return now


def time_to_deadline():
	datetime (input('введите год')
		input(''))

	deadline = input
	datenow = datetime.now()
	
	delta = date - deadline
	if date == deadline:
		print('Дедлайн сегодня')
	elif date < deadline:
		print ('До дедлайна ', delta.days,' дней')
	elif date > deadline:
		print('Дедлайн был ',delta.days, ' дней назад')






rename_current_day_to_russian()

time_to_deadline()