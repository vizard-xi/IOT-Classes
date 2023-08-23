def stars():
    for i in range(1,5):
        print ("*" * i)
        
    for j in range(3,0,-1):
        print("*" * j)

stars()

def evens1(listnum):
    sum1 =0
    for i in listnum:
        if i % 2 == 0:
            sum1 += i
    print(sum1)
    
tryw = []
yes = True
while yes:
    num = int(input("Enter your number "))
    tryw.append(num)
    again = input("Do you want to go again ")
    again = again.lower()
    if again == "yes":
        yes = True
    else:
        yes = False
print(tryw)
evens1(tryw)

            
            
