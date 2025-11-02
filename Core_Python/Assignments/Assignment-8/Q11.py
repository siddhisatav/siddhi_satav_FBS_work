# 11. WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.


def Armstorng_Num():
    num =int(input("Enter a number : "))
    digits = len(str(num))
    
    temp =num 
    sum_power = 0 
    while temp > 0 :
        digit = temp % 10
        sum_power += digit**digits
        temp =temp // 10
    if num == sum_power :
        print (num, "is Armstrong Number")
        
    else:
        print(num , "is not Armstrong Number")
        
Armstorng_Num()