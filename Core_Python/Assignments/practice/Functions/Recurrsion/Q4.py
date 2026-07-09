def seperate_digit(num):
    if(num <= 0 ):
        pass
    else :
        d = num % 10 
        print(d)
        num = num // 10 
        seperate_digit(num)
        
n = int(input("enter number : "))
seperate_digit(n)
         