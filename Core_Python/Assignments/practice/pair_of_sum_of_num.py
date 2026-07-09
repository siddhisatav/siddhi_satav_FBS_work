li1 = [2,5,9,11,20,1,6,4,3]
num=7
li1.sort()
# print(li1)

ans=[]
for i in range(len(li1)):
    

         for j in range(i+1,len(li1)):
             
             if li1[i] + li1[j] == num :
                 ans.append((li1[i] , li1[j]))
                 
            
             
             
print(ans)
             
        