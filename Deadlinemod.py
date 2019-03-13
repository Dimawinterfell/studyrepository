from datetime import datetime, timedelta, date
import time

now = datetime.now()
print(now)

deadline = datetime( 
	int(input('god ')),
	int(input('mesyac ')),
	int(input('den ')))
delta = deadline.date() - now.date()

if delta.days > 0:
	print('do dedlaina ostalos', delta.days,'dney')
elif delta.days <0:
	print('Posle dedlaina proshlo', -delta.days, 'dney!')
else:
	print('Dedlain Segodnya!')