# 2. Write a program to find maximum and minimum element in a list.

def element(li):
    for i in range(len(li)):
        max=li[0]
        min = li[0]
        
        if max < li[i]:
            max = li[i]
            
            
        if min > li[i]:
            min = li[i]
            
            
    return [min ,max] 


li =[1,2,3,4,5]
result = element(li)

print("Maximum element is : ",result[1])

print("Maximum element is : ",result[0])
