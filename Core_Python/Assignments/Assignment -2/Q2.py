# Write a program to swap two numbers using third variable.
# Write a program to swap two numbers without using third variable.

a = int(input("enter a :"))
b= int(input("enter b :"))
print("before swapping")
print(a , b)
a =b^a
b=a^b
a=a^b

# a= a+b
# b=a-b
# a=a-b

print("After Swapping :")
print(a ,b)


