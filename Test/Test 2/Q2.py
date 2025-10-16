num = int(input("enter tree digit number : "))
digit3 = num % 10
digit2 = (num % 100 ) //10
digit1 = num // 100
if digit1 == 2*digit2 and digit1 == digit3/2 :
    print("Yes,you have done it !!!! ")
    
else:
    print("please try next time!")