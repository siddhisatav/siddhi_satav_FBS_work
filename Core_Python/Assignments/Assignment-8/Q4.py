# 4. Sum of all odd numbers between 1 to n

def Sum_odd_num(n):
     sum_num = 0 
     for i in range (1,n+1):
        if i % 2 != 0:
            sum_num+=i
            
     print(f"Sum of {n} Odd numbers is : { sum_num }")
     
     
n =int(input("Enter value of n : " ))
Sum_odd_num(n)