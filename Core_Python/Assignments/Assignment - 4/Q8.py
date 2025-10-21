# 8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

n = int(input("Enter a value of n : "))
print("Numbers divisible by 7 and multiple of 5  : ")
for i in range (0,n+1):
    if (i %7 == 0) and (i % 5 == 0):
        print(i)
        
        