# 10. Write a program to reverse three-digit number.

num =int(input("enter num :"))

digit1 = num//100
digit2 = (num//10)%10
digit3 = num%10
    
rev = digit3*100+digit2*10+digit1
    
print("reversed num : ", rev)
    
    