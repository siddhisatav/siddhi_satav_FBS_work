# 6. Write a program to remove duplicates from the list.


def removeDuplicate(li):
    unique_li = [0]*len(li)
  
    u =0
    for i in range (len(li)):
        item = li[i]
        found = False 
        for j in range(u):
            if unique_li[j] == item:
                found = True
                break
        if not found:
                unique_li[u]=item
                u+=1
                
    return unique_li







li= [34,44,55,23,55,44]
print(li)
result = removeDuplicate(li)
print(result)