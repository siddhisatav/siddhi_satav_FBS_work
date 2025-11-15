# 4. Write a program to find sum of n numbers using recursion.


def sumNum(n):
    if n == 0:
        return 0
    return n+sumNum(n-1)

n=int(input("enter value of n : "))
result = sumNum(n)
print(result)