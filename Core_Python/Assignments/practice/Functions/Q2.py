def maxelement(li):
    max=li[0]
    for i in range(0,len(li)):
        if(max < li [i]):
            max= li[i]
    return max
            
            
li=[24,65,43,456,23,43,23,33,44,12]
max_ele = maxelement(li)
print("minimum element is", max_ele )