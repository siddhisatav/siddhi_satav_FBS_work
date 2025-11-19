# 5. Python Program to Sort a List According to the Length of the Elements
# within the list.

def sortElement(li):
    size = len(li)
    for i in range (1,size):
        for j in range (0,size-i):
            if len(li[j]) > len(li[j+1]):
                li[j],li[j+1] = li[j+1],li[j]
                
    return li

li = ["santosh","satav","patil","sid"]
print("Before sorting ", li)
result = sortElement(li)
print("After sorting according to the length of element : ", result)
                