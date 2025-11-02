# 6. Write a program to find print the following Fibonacci series using
# functions:
# 1 1 2 3 5 8 n terms


def fibonacci(n):
     a =0
     b=1 
     for i in range(1,n+1):
        a,b=b,a+b
        print(a,end=" ")
        
n =int(input("enter value of n : "))
fibonacci(n)
    