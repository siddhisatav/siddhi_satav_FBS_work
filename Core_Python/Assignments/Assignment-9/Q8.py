# 8. Write a program to check whether a number is prime or not using recursion.

def isPrime(n,i=2):
    if n <= 1:
        return False
    if i == n:
        return True 
    if n % i ==0:
        return False
    return isPrime(n,i+1)

n =int(input("enter a number"))
if isPrime(n):
    print(n,"is a prime number")
    
else:
    print(n,"is not a prime number ")