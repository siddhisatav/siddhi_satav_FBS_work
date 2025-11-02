# 5. Sum of all prime numbers between 1 to n

def sum_prime_num (n):
    sum_Prime_num =0 
    
    for i in range (2, n+1):
      is_prime = True
      for j in range (2,int(i**0.5)+1):
        if i % j == 0:
           is_prime = False
           break
      if is_prime:
         print(i,end=" ")
         sum_Prime_num +=i
         print("Prime numbers : ", i )
            
    print("Sum of prime numbers is : ", sum_Prime_num)
    
    
    
n = int(input("Enter value of n " ))

sum_prime_num(n)