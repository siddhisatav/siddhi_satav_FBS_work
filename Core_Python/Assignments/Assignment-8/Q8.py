# 8. Write a program find reverse of a number

def reverse_num():
    num =int(input("enter number : "))
    temp = num
    rev = 0 
    while num > 0 :
        digit = num % 10 
        rev = rev * 10 + digit
        num = num//10
    print("Reverse of " , temp , "is : ",rev  )
    
reverse_num()