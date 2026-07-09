
def wave(arr):
     size=len(arr)
     for i in range(len(arr)-1):
         if (i>0 and arr[i] < arr[i-1]):
             arr[i],arr[i-1] = arr[i-1],arr[i]
        
         if (i<size-1 and arr[i+1] > arr[i]):
             arr[i],arr[i+1] = arr[i+1],arr[i]
        
     return arr
 
 
arr = [5,1,3,2,4]
ans=wave(arr)
print(ans)