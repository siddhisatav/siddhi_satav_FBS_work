def insertionSort(li):
    size=len(li)
    for i in range(1,size):
        temp =li[i]
        
        j=i-1
        
        while j >= 0 and li[j] > temp:
            li[j+1] = li[j]
            j -= 1
            
        li[j+1] = temp
        
    return li

li=[8,9,7,10,6,5]
print(li)
ans = insertionSort(li)
print(ans)