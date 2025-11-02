for i in range (1,6):
    print(" " * (6-i) , end= " ")
    
    for j in range ( 1,i+1):
        if  j == 1 or i==j:
            print("*" , end= " ")
            
        else:
            print(" ", end=" ")
            
            
            
    print()
            
for i in range (4,0,-1):
    print(" " *(6-i),end=" ")
    
    for j in range (1,i+1):
        if j==1 or i==j:
            print("*" , end=" ")
            
        else:
            print(" ",end=" ")
            
    print()
    