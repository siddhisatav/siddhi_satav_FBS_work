def sumofnum(n):
    if (n == 0):
        return 0
    elif n < 0 :
         return n + sumofnum(n+1)
   
n = int(input("enter value of sum of series : "))
result = sumofnum(n)
print(result)