# 10. WAP to check if given number is Perfect Number.

num =int(input("Enter a number : "))
sum =0
for i in range (1,num):
    if (num % i == 0):
        print(i)
        
        sum =sum + i
    
if sum == num :
    print(f"\n{num} is a Perfect number ")

else:
    print(f"{num} is not Perfect number")
    