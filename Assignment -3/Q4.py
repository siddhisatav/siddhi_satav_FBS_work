#4. Write a program to input all sides of a triangle and check whether triangle is valid or not

 
a = float(input("enter first side: "))
b = float(input("enter second side : "))
c = float(input("enter third side : "))

if(a+b>c ) and (a+c > b) and (b+c > a):
    print("IT is valid triangle.")
    
else:
    print("it is not vaild triangle.")