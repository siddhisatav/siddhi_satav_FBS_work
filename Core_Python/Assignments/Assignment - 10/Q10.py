# 10. Write a program to remove all occurrences of a given element in the list.

def remove_target(li,target):
    new_li=[0]*len(li)
    n =0
    for i in range (len(li)):
        if li[i] != target:
             new_li[n]=li[i]
             n+=1
             
    return new_li

li=[3,4,5,6,7,6]
target = 6
print(li)
result = remove_target(li,target)

print(result)

            
        
   
    
    