# 4. Python Program to Find the Second Largest Number in a List Using Bubble
# Sort

def bubbleSort(li):
    size = len(li)
    for i in range(1,size):
        for j in range (0,size-i ):
            if li[j] > li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
                
    return li[size-2]

li = [33,2,70,5,6,7,40]
print("List before sorting : ", li)
result = bubbleSort(li)
print("List after sorting ", li)

print("Second largest element : ", result)
