arr=[5,32,45,4,12,18,25]

def sort_element(arr):
    for i in range(1,len(arr)-1):
        for j in range(0,len(arr)-i):
            if (arr[j] > arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return (arr)     


def diff(arr):
    
    ele_diff=0
    for i in range(len(arr)-1):
        d = arr[i+1]-arr[i]
        print(d)
        if ele_diff == 0 :
            ele_diff=d
            
        elif ele_diff > d:
            ele_diff = d
            
        

       
    return (ele_diff)

        
        
ans = sort_element(arr)
res=diff(ans)
print(res)


   
        