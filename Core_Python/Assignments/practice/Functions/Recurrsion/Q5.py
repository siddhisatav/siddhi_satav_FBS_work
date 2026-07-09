def sumdigit(num):
    if num <= 0 :
        return 0 
    else:
        return (num %10) + sumdigit(num // 10)

n= int(input("enter number : "))
print(sumdigit(n))