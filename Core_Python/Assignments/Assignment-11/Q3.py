# 3. Python Program to Sort the List According to the Second Element in Sublist


def sortList(li):
    size = len(li)
    for i in range(0,size):
        for j in range(0,size-i-1):
            if li[j][1] > li[j+1][1]:
                li[j],li[j+1] = li[j+1],li[j]
                
    return li


li =[ [2,5], [1,3], [6,1], [4,8] ]
print("Before sorting : ", li)
result = sortList(li)

print("After sorting ", result)

                