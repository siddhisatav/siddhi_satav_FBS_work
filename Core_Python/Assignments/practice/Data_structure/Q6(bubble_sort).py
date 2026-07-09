def bubbleSort(li):
    size = len(li)
    for i in range (1,size):
        for j in range(0,size - i):
            if (li[j] > li[j+1]):
                li[j],li[j+1]=li[j+1],li[j]
    return li 
    
    
li = [25,30,59,22,10,44]
print("Before sorting : ", li)
result = bubbleSort(li)
print("After sorting : " , li )
                
            