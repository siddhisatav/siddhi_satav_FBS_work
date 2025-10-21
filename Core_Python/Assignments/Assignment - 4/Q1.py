# 1. WAP to print all even numbers until n.

n =int(input("enter count of even numbers you want : "))
 
print("Even Numbers")
for i in range (0 , n+1):
       
    if(i % 2 ==0):
        
        print(i)
   
    