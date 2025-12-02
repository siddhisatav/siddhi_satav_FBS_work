def factors(num):
    factor = [ ]
    for i in range(1 , num+1):
        if num % i == 0:
            factor.append(i)
    return factor
        
num = int(input("enter number : "))
ans = factors(num)
print(ans)