# 5. Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount. (Use looping to optimize
# the problem)

amount = int(input("enter amount : "))
Notes = [2000,500,200,100,50,20,10,5,2,1]

for i in Notes:
    if amount >= i :
        count = amount // i
        amount = amount % i 
        
        print(f"{i} * {count}")