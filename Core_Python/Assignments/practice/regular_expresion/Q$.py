li = [2,3,5,6]
n=len(li)+1
totalsum = (n*(n+1))//2
sum=0

for i in range (len(li)):
    sum +=li[i]
    
    
missingnum = totalsum - sum 
print(missingnum)

