# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
#  times. After that program to terminate. 


chance = 3 
password_code = 1234
id = "siddhi"
userid = input("enter your user id : ")
password = input("enter your password : ")

while chance != 0 :
    if (id != userid) and  ( password_code != password):
        print("Incorrect user id or password !!!!")
        print(f"please try again , you have {chance} chance left.... ")
        userid = input("enter your user id : ")
        password = input("enter your password : ")
        chance -=1
    else:
      print("Sucessfully login")
      break
        
    

         