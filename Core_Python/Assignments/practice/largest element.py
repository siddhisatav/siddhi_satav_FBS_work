
def maxx_element(Arr):
   max=Arr[0]
   for i in range(len(Arr)):
        if (Arr[i] > max):
            max=Arr[i]

   return max

Arr=[2,3,2,6,5,15]
ans=maxx_element(Arr)
print(ans)



    
