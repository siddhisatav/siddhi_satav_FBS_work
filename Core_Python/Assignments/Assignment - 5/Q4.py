# 4. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)

num = int(input("enter a number  :"))
temp = num 
sum_digit = 0
order = len(str(temp))
while temp != 0 :
    digit = temp % 10 
   
    sum_digit += digit**order
    temp //= 10 
        
if sum_digit == num :
    print("Armstrong number ")
    
else:
    print("Not Armstrong number")