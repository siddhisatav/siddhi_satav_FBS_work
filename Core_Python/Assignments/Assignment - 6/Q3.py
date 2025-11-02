# c.

for i in range(1,5):
   
    print(" "*(5-i),end= " ")
        
    for j in range (1,i+1):
        if j==1 or j==i:
            print(1,end=" ")
            
        elif i==3 and j == 2:
            print(2,end=" ")
            
        elif i==4 and (j == 2 or j==3):
            print(3,end=" ")
            
    print()
    
    
    
