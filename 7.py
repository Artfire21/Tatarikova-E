n = int(input('Вводится первое число Фибоначчи -  '))
mass = [ ]
feb = n**(n+1)-n**(n+2)

for i in range(n):
	if  i>feb:
		mass.append(i)

print(mass)

