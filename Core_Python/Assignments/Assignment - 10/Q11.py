# 11. Write a program to print all numbers which are divisible by m and n in the
# list.

def divisible(li,m,n):
    ans = []
    
    for i in li:
        if i % m == 0 and i % n == 0:
            ans.append(i)
            
    return ans

li=[76,89,654,77,4,79,8]
n=int(input("enter value of n :"))
m = int(input("enter value of m :"))
result = divisible(li,m,n)
print(f"number divisible by {m} and {n} is : {result}")