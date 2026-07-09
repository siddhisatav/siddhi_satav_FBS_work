def binarysearch (li,searchele):
    start = 0
    end =len(li)-1
   
    while (start <=end ):
             mid = (start + end )//2
       
             if (li[mid] < searchele) :
              
                 start = mid +1
              
             elif (li[mid] > searchele) :
                
                 end = mid - 1
               
             elif (li[mid] == searchele) :
                 return mid
             
    else :
        return -1 
    

        
li = [23,30,40,50,60]
searchele = 30
result = binarysearch(li , searchele)
print (result)
