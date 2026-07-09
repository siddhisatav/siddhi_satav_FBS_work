def max_sub_sum(arr):
    curr_sum = 0 
    max_sum = 0
    sub=[]
    for i in range (len(arr)):
          curr_sum = curr_sum + arr[i]
          if curr_sum > max_sum :
             max_sum = curr_sum
             sub.append(arr[i])

          if curr_sum < 0 :
             curr_sum = 0
            
    return max_sum, sub

arr = [-4,-3,-2,2,3,1,-2,-2,6,-6,-4,2,1]
result = max_sub_sum(arr)
print(result)