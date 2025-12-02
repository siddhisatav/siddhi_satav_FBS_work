def factorial(num):
    if num == 0 or num == 1:
        return 1 
    return num * factorial(num-1)

num = int(input("enter number : "))
ans = factorial(num)
print(ans)