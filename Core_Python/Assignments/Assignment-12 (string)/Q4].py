# 4. Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged

def newString(str):
    
   if len(str) <= 1 :
       return str
   return str[-1]+str[1:-1]+str[0]


str= input("enter your string : ")
ans = newString(str)
print(ans)
        
    
