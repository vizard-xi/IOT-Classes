def roman(num):
	number = [1000,900,800,700,600,500,400,300,200,100,90,80,70,60,50,40,30,20,10,9,8,7,6,5,4,3,2,1]
	value = ["M","CM","DCCC","DCC","DC","D","CD","CCC","CC","C","XC","LXXX","LXX","LX","L","XL","XXX","XX","X","IX","VIII","VII","VI","V","IV","III","II","I"]
	
	i = 0
	rn = []
	
	
	while i < len(number)-1:
		div = num // number[i]
		num %= number[i]
		roman = value[i]*div
		rn.append(roman)
		i+=1
	return "".join(rn)

number = int(input("Please input your number to convert: "))	
print(f"{number} in roman numerals is {roman(number)}")
