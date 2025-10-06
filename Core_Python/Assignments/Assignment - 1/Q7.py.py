# 7. Program to Find the Roots of a Quadratic Equation
import cmath
a= float(input("enter coefficient a: "))
b= float(input("enter coefficient b: "))
c= float(input("enter coefficient c: "))

n = (b**2)-(4*a*c)

root1= (-b + cmath.sqrt(n))/ (2*a)
root2=(-b - cmath.sqrt(n))/(2*a)

print("Root1 : ", root1)
print("Root2 :", root2)