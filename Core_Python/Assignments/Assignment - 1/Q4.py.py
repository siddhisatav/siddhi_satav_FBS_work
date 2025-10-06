# 4. Write a program to enter P, T, R and calculate simple Interest.

P = int(input("enter principal amount : "))
T =int(input("enter time (year) :"))
R =int(input("enter Rate : "))

simple_interest = P*T*R/100

print("Simple interest :", simple_interest)
