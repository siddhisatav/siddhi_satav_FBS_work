# write a program to find the area and perimeter of following fig
l=float(input("enter the length"))
b=float(input("enter the breadth"))
r=float(input("enter the radius"))

area= (l*b) + (1/2*3.14*r*r)
perimeter=(2*(l+b)) + ((3.14*r)+2*r)
print("Area : ",area)
print("Perimeter :" , perimeter)