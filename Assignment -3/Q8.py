# 8. Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the 
# same. If user enters the same number then show him success message otherwise failed. (Something like captcha)

import random
pass1 = "user"
username1 = "Sid"
pass2=input("enter password : ")
username2 =input("enter Username :")


# checking password and username is correct or not 
while(pass1 != pass2 or username1 != username2):
    
    print("incorrect username or password ..! \nplease re-enter password and username ")
    pass2=input("enter correct password :")
    username2=input("enter correct username : ")
    
    
else :
    print("correct username and password !!!!")
    
    
    # generating random 4 digit number as captcha
    captcha = random.randint(1000,9999)
    print("Captcha : ",captcha)

    getcaptcha = int(input("Enter above captcha : "))
    
    
    if captcha == getcaptcha :
      print("login Successfull.")
    
    else:
      print("login failed")
    
    
    
