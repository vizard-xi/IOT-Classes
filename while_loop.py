
	
def evens(num1,num2):
	if num1 %2 == 0:
		i = num1
		while i < num2:
			print(i)
			i +=2
	else:
		i = num1+1
		while i < num2:
			print(i)
			i +=2
	
#evens(2,29)

def reverse_evens(num1,num2):
	if num1 %2 == 0:
		i = num1
		while i > num2:
			print(i)
			i -=2
	else:
		i = num1+1
		while i > num2:
			print(i)
			i -=2

#reverse_evens(30,2)

def evens2(num1,num2):
	if num1 %2 == 0:
		for i in range(num1, num2, -2):
			print(i)
	else:
		num1 = num1 + 1
		for i in range(num1, num2, -2):
			print(i)

evens2(20,1)
