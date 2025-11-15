# 6. Write a program to print Fibonacci series using recursion.

def fib(n):
    if n ==0 :
        return 0 
    elif n == 1:
        return 1
    else:
          return fib(n-1) +fib(n-2)
      
num = int(input("Enter n: "))
print("Fibonacci series up to", num, "terms:")
for i in range(num):
    print(fib(i), end=" ")
