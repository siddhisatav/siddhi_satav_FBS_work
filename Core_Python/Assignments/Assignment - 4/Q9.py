# 9. WAP to print all numbers in a range divisible by a given number.

n = int(input("Enter value of n : "))
num = int(input("Enter number : "))
print(f"Numbers divisible by {num} : ")
for i in range (1,n+1):
    if i % num ==0 :
        print(i)