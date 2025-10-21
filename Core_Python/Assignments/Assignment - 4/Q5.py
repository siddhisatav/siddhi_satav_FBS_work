# 5. WAP to print Fibonacci series upto n.
n = int(input("enter value of n :"))
a,b=0,1
for i in range (0 , n+1):
    print(a)
    a,b=b,a+b
    
   