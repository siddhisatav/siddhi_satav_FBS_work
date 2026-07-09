def maxElement(li):
    max = li[0]
    smax=0
    for i in range (0,len(li)):
        if(max < li[i]):
            smax =max
            max=li[i]
        elif smax < li[i]:
                smax = li[i]
                
    return max , smax

li = [24,35,46,55,44,10]
result = maxElement(li)
print (result)
                
                
        