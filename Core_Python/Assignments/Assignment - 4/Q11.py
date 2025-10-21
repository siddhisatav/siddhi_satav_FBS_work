# 11. WAP to check if given number Strong Number.
sum_fact = 0
num = int(input("Enter number: "))
temp = num

while temp > 0:
    digit = temp % 10         
    factt = 1                 

    for i in range(1, digit + 1):
        factt *= i             
    sum_fact += factt         
    temp //= 10               

# Check if number is Strong Number
if num == sum_fact:
    print("Strong Number")
else:
    print("Not a Strong Number")
