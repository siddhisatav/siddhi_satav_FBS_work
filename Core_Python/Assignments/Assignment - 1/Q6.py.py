# 5. Write a program to enter P, T, R and calculate Compound Interest.

P = int(input("enter principal amount : "))
T =int(input("enter time (year) :"))
R =int(input("enter Rate : "))

compound_interest= P*(1+R/100)**T

print("Compound Interest : ",compound_interest )