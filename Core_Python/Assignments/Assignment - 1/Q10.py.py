# 10. Write a program to calculate area of an equilateral triangle.
import cmath
a = int(input("enter sides of equilateral triangle : "))

Area = (cmath.sqrt(3) / 4 )* (a**2)

print (Area)