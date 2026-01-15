# 1. We want to generate Fibonacci numbers up to a certain limit.
# Instead of computing and storing the entire sequence in memory,
# create generator to yield Fibonacci numbers one by one,
# conserving memory and allowing for easy iteration.

def fib (n):
    a,b = 0,1 
    for i in range(n):
        yield a
        a,b=b,a+b
        
n = int(input("Enter number of terms: "))
for num in fib(n):
    print(num, end=" ")
