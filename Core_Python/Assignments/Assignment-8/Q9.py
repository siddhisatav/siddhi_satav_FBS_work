# 9. Write a program to check if entered number is a palindrome or not.

def palindrome_check ():
    num = int(input("Enter number : "))
    temp = num
    rev = 0 
    while (num > 0 ):
        digit = num % 10 
        rev = rev * 10 + digit 
        num = num // 10     
        
    if (temp == rev ):
        print("Number is Palindrome  ")
    else:
        print("Number is not Palindrome")
        
palindrome_check()
    
