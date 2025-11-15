# 2. Write a program to check if given number is Armstrong or not using recursive
# function.


def digitSep ( n ):
    if n < 10 :
        return [n]
    
    return digitSep(n//10)+[n%10]
   
def Armstrong(n):
   
    d = digitSep(n)
    power = len(d)
    
    def powerSum(dlist):
        if len(dlist ) == 0:
            return 0
        
        return dlist[0] ** power + powerSum(dlist[1:])
    
    return powerSum(d) == n


n = int(input("enter a number : "))
if Armstrong(n):
    print(n , "is an Armstrong number")
    
else:
    print(n,"is Not an Armstrong number")