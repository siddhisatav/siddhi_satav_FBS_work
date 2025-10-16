# 3. Write a program to input angles of a triangle and check whether triangle is valid or not.

angle1=int(input("enter angle1 : "))
angle2=int(input("enter angle2 : "))
angle3=int(input("enter angle3 : "))

sum = angle1+angle2+angle3

if sum == 180 :
    print("Angles are valid ")
    
else:
    print("Angles are not vaild")
    