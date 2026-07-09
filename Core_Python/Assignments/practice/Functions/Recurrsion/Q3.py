def factorial ( n ):
    if n == 0 :
        return  1
    elif (n < 0 ):
        return f"{n } is an negative number "
    else:
        return n*factorial(n-1)

n= int(input("enter value of n : "))
ans = factorial (n )
print(ans)             