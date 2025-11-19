# 9. Write a program to create three lists of numbers, their squares and cubes



def fun(li):
        square=[]
        cube=[]
        for i in range (len(li)):
               square.append(li[i]**2)
               cube.append(li[i]**3) 
             
        return square,cube            
 
li=[]
for i in range(5):
        element = int(input("Enter number in list  : "))
        li.append(element)
print("Your list :",li)
ans = fun(li)
print("Square of element in list: ", ans[0])
print("cube of element in list: ", ans[1])
        
        