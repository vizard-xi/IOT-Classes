def calculate(num1,num2,operator):
	if operator == "add" or operator=="ADD":
		answer = num1 + num2
	elif operator == "subtract" or operator=="SUBTRACT":
		answer = num1 - num2
	elif operator == "multiply" or operator == "MULTIPLY":
		answer = num1*num2
	elif operator == "divide" or operator == "DIVIDE":
		answer = num1/num2
	else:
		answer = "Invalid operator"
	return answer
	
number1 = int(input("Enter your first number "))
number2 = int(input("Enter your second number "))
operator = input("Enter your prefered operation in words ")
print(calculate(number1,number2,operator))

