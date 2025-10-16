a=float(input("enter first side : "))
b=float(input("enter second side : "))
c=float(input("enter third side : "))

if (a+b > c) and (a+c >b) and (b+c >a):
    if a==b or a==c or b==c :
        print("triangle is Isosceles. ")
        
        
    elif a==b==c :
            print("triangle is Equilateral. ") 
            
    else:
            print("triangle is Scalene. ")
            
else:
        print("triangle is not vaild. ")