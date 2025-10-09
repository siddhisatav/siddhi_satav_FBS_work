# 10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

age = int(input("enter your age :"))
print("enter 1 for female \nenter 2 for male .")
gender = int(input("enter your gender : "))

if gender == 1 and age >=18 :
    print("Eligible to marry")
    
elif gender == 2  and age >=21 :
    print("Eligible to marry") 
    
else :
    print("Not Eligible to marry")