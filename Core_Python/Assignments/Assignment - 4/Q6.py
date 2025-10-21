# 6. WAP to check if a given number is prime number or not.
num =int(input("Enter a number : "))

for i in range (2,num):
    if num % 2 != 0:
        print("Number is prime ")
        break
    
    
else:
  print("Number is not prime")