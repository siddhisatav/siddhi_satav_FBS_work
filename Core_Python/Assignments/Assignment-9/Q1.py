# 1. Write a program to find sum of following series using recursive functions:

# i. 1! + 2! + 3! + 4! +..... + n!

def factorial(i):
  
         if i == 0 or i==1:
            return 1
    
         else:   
              return  i * factorial(i-1)


def sumOfNum(n):
    if n == 1:
        return factorial(1)
    return factorial(n)+sumOfNum(n-1)
       
          
n = int(input("enter value of n :"))
result = sumOfNum(n)
print(result)
        
        
    
     
    
    
    