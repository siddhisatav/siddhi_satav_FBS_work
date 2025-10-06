# 7. Find the sum of three-digit number.

num =int(input("Enter num :"))

sum=0
while num > 0:
    digit = num% 10
    sum += digit
    num //= 10

print("sum :" , sum)
    
    

    
    