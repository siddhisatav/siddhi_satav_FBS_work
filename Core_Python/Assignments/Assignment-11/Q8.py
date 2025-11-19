# 8. Print 1 to 100 in snakes and ladder pattern.

def snake():

    num =100
    
    reverse = True
    for i in range (10):
        ans=[]
        if reverse:
            for j in range (num,num-10,-1):
              ans.append(j)
            
        else:
            for j in range (num-9,num+1):
                ans.append(j)
             
        print(ans)
    
        num-=10
        reverse = not reverse
    
        
        
     
anss=(snake())

