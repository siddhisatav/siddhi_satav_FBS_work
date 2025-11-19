# 7. Write a program to create a new list from existing list which contains cube of
#  each number of list.


def cube(li):
    cude_li=[0]*len(li)
    u=0
    for i in range(len(li)):
        cude_li[i]=li[i]*li[i]*li[i]
        
    return cude_li
    
li=[4,3,5,2,1,5,6]
result = cube(li)
print(result)