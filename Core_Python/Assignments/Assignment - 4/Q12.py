# 12. WAP to print Armstrong number within a given range

n= int(input("enter num :"))
temp = n
# for i in range(n):
order = len(str(n))

summ=0
while temp != 0:
    digit = temp%10
    
    summ += digit ** order
    temp //= 10
    
if summ == n :
    print(f"{n} is a armstrong")
    
else:
    print(f"{n} is not armstrong")
    
        
    

