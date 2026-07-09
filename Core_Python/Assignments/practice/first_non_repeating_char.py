# strr="netsetosnetm"
# uni=[]
# count=[]
# for i in range (len(strr)):
#     for j in range (i+1,len(strr)):
#         if strr[i] == strr[j]:
#             count.append(strr[i])
            
            
# print("count arr",count)
            
# for k in strr:
#     if k not in count:
#         uni.append(k)
        
        
# print("unique ele",uni[0])
        
        
        
        

        
            
def f_non_rep(s): 
       
        dup={}


        for i in range(len(s)):
            key=s[i]
            if key in dup:
                dup[key] +=1
            else:
                dup[key] = 1
                
        for j in range(len(s)):
            if dup[s[j]] == 1:
                return(s[j],j)
            
s="netsetosnetm"
ans=f_non_rep(s)
print(ans)             
   
        
        