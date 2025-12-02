# sum of 1/1! + 2/2! + 3/3! ... n / n !

def fun(n):
    fact =1
    total = 0 
    
    for i in range(1,n+1):
        fact = fact *i
        num = i/fact
        total+=num
        
    print(total)
    
    
n =int(input("Enter value of n "))
fun(n)

        
    