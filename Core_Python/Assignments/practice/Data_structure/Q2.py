def linearsearch(li , searchElemet):
    for index in range(0,len(li)):
        if(li[index]==searchElemet):
           return index
        else:
           return -1
            
li = [23,39,70,36,53,89]
ele = 23
result = linearsearch (li , ele)
if result != -1 :
     print (f"{ele} is present at index : {result}")
else :
     print (f"{ele} is not present in list ")
     
     
#time complexity
# best = O(1)
# worst = O(n)
# Average = O(n)