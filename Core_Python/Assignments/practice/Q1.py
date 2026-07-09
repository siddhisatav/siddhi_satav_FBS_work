def Check_prime(n):
    isprime = False
    for i in range ( 2 , n):
    
        if n % i == 0 :
             isprime = False
             break
        else:
            isprime = True
    if isprime == True :
        return True 
    
    else :
        return False          
          
                
n =int(input("enter num"))
ans = Check_prime(n)
print (ans)


def chechPrime(num):
    if num <=1:
     for i in range(2,num // 2 +1) :
         if(num % i == 0):
              return False
     else:
        return True
    
    
n =int(input("Enter number to check it is prime or not : "))
ans = chechPrime(n)
if ans :
    print("it is prime number")
else:
    print("it is not prime number ")