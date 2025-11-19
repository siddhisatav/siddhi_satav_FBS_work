# 10. Write a program to print list after removing even numbers.

def removeEven(li):
    for i in range (len(li)-1,-1,-1):
          if li[i] % 2 == 0 :
             li.pop(i)
             
    return li
        


li=[]
for i in range(5):
        element = int(input("Enter number in list  : "))
        li.append(element)
print("Your list :",li)
ans=removeEven(li)
print("List after removing even numbers : ",ans)