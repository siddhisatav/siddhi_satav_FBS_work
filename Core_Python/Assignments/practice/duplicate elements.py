arr=[1,1,2,2,2,3,4,4,4,5,5,2]
# 1st approch

# arr1=[set(arr)]
# print(arr1)

# 2nd
arr3=[]

for i in range(len(arr)) :
   
    if arr[i] not in arr3:
        arr3.append(arr[i])
        print(arr3)
print(arr3)

# 3rd
n=len(arr)
temp=[0]*n
pivot = 0 
for i in range(0, n-1):
    if(arr[i] != arr[i+1]):
        temp[pivot] = arr[i]
        pivot+=1
        
temp[pivot] = arr[n-1]

print(temp)
            

        
        