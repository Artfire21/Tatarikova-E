x = int(input('Первый элемент - '))
d = int(input('Разность - '))

mass = [ ]

for i in range(x, 100, d):
	mass.append(i)

print(mass)
