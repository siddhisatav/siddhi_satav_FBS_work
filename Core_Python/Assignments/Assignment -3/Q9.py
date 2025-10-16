# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

DBMS = int(input("enter marks of DBMS : "))
CN = int(input("enter marks of CN : "))
OOPS = int(input("enter marks of OOPS : "))
MATHS = int(input("enter marks of MATHS : "))
ML = int(input("enter marks of ML : "))

percentage = ((DBMS + CN + OOPS + MATHS + ML ) / 500) * 100

print("Percentage :",percentage,"%")

if percentage < 35 :
    print("Fail")

elif percentage > 35 and percentage < 50 :
    print("Third class ")
    
elif percentage > 50 and percentage < 70 :
    print("Second Class ")
    
elif percentage > 70 and percentage <80 :
    print("First Class") 
    
else:
    print("Distinction")