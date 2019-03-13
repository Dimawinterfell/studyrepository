def func(tooth,depht,material):

	print('Пациент обратился с жалобами на кариес в',tooth, 'зубе')
	print('Диагноз: Хронический',depht,'кариес',tooth,'зуба')
	print('Лечение: Осмотр,некротомия,',material)

	checkTooth = int(input('Зуб>>>'))
	checkDepht = input('Глубина>>>')
	checkMaterial = input('Материал>>>')

func(tooth=checkTooth, depht=checkDepht, material=checkMaterial)





