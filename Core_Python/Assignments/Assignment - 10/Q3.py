# 4. Python Program to Find the Second Largest Number in a List Using Bubble
#  Sort

def bubbleSort(li):
    for i in range(1,len(li)):
        for j in range(0,len(li) - i ):
            if (li[j] > li[j+1]):
                li[j],li[j+1] = li[j+1] , li[j]
    return li


li =[12,33,11,45,90,70]
result = bubbleSort(li)
size= len (li)
print(result)
print("Second largest Element : ", result [size - 2 ])
