def num(a):
    i=0
    res=0
    while (i<len(a)):
        curr=value(a[i])
        if(i+1<len(a)):
            next=value(a[i+1])
            if(curr>=next):
                res=res+curr
                i=i+1
            else:
                res=res+next-curr
                i=i+2
                
        else:
            res=res+curr
            i=i+1   
    return res
    
    
    
def value(a):
    if (a=='I'):
        return 1
    if (a=='V'):       
        return 5
    if (a=='X'):
        return 10
    if (a=='L'):
        return 50
    if (a=='C'):
        return 100
    if (a=='D'):
        return 500
    if (a=='M'):
        return 1000
    
    
    
ans=num("MCMXCIV")
print(ans)