# 1. write a program to print n prime number

def fun(n):
     for i in range(2,n):
        for j in range(2,i):
             if i % j == 0:
                 break
        else:
            print(i,end=" ")
                 
                 
n =int(input("Enter value of n : "))
fun(n)
                 
                  
                    
                 
            
