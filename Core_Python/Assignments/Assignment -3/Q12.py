# 12. Write a program to check if given 3 digit number is a palindrome or not.

num =int(input("enter number : "))

hundred = num//100
tens = (num//10)%10
unit = num%10

if hundred == unit:
    print("** Number is palindrom **")
    
else:
    print("Number is not palindrom")