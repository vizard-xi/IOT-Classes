def func(min,max):
	list = []
	if min % 2 == 0:
		for i in range(min,max,2):
			list.append(i)
		return list
	else:
		min = min +1
		for i in range(min,max,2):
			list.append(i)
		return list
		
print(func(1,30))

