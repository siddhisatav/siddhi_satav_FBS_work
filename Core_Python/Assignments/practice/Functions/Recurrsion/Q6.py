 
def fact (num):
    if num == 0:
        return 1 
    else:
        return num * fact(num-1)
    
   
def strong (num):
    if num <= 0 :
        return 0
    else:
        d = num%10
        f = fact(d)
        return f + strong(num // 10)
        
    
    
num = int(input("Enter a number : "))

result = strong(num)
if result == num :
    print(f"{num} is strong number  ")
else:
    print("is not strong number ")