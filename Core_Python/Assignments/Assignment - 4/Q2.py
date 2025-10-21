# 2. WAP to print all odd numbers until n.

n =int(input("enter count of odd numbers you want : "))
 
print("Odd Numbers")
for i in range (0 , n+1):
       
    if(i % 2 !=0):
        
        print(i)
   
    