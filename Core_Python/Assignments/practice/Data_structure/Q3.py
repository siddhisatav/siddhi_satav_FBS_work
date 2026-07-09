def minElement(li):
    min = li[0]
    for i in range (0 ,len(li)):
        if(min > li[i]):
            min = li[i]
    return min
    
li = [34,56,55,32,23,22,11]
result = minElement(li)
print("Minimum element is  : " ,  result)

            