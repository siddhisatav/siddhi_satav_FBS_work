# 4. Write a program to reverse the list.

def Reverse(li):
    size = len(li)
    s = 0
    e=size -1
    
    while (s < e):
        li[s],li[e] = li[e],li[s] 
        s+=1
        e-=1
        
        
    return li 
    
    
li = [2,3,4,5,6,7,8]
print("Before Reversing list : ",li)
result = Reverse(li)
print("After Reversing list :", result)

       
        