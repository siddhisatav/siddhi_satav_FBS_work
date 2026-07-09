# Validate user name 
def validate(str):
    for i in str :
         if not(i.isalpha() or i.isspace()) :
             return False
    
    return True
     
str = input("enter your name : ")
ans =validate(str)
if ans == True:
    print("congratulations ....You enterrd a valied name ")
    
else:
    print("Please enter valid name !!!!!!!")