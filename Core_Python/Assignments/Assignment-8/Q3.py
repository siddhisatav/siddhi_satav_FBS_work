# 3. Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
#  c. 1^1 + 2^2 + 3^3+ ...... n^n

def sum_n(n):
    sum_num=0

    for i in range(1,n+1):
      sum_num += i
      
    print("Sum of numbers is : ", sum_num)
   
   
def sum_factorial(n):
    fact =1
    sum_fact=0
  
    for i in range(1,n+1):
        fact=fact*i
        sum_fact +=fact
    print("Sum of Factorial is : ", sum_fact)
    


def sum_power(n):
    sum_power=0
 
    for i in range(1,n+1):
      power =i**i
      sum_power +=power
    print("Sum of Power of Number is : ", sum_power)
 

   
n = int(input("Enter value of n: "))
sum_n(n)
sum_factorial(n)
sum_power(n)
    
    