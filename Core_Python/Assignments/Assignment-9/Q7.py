# 7. Write a program to find sum of digits using recursion.
def sumDigit(n):
    if n == 0:
        return 0 
    return n%10+sumDigit(n//10)



n =int(input("enter number :"))
result =sumDigit(n)
print(result)