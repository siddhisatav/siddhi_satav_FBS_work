def selectionSort(li):
    size = len(li)
    for i in range (0,size-1):
        min = i 
        for j in range(i+1,size):
            if li[min] > li[j]:
                min = j
                
        li[min],li[i]=li[i],li[min]
        
    return li

li=[24,55,64,34,23,2]
print("List before sorting :" , li)
ans = selectionSort(li)
print("List after sorting :", ans)
        
                