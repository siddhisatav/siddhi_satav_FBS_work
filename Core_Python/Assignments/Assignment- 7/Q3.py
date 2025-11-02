for i in range ( 1,6):
    
    for j in range(1,7-i):
        print(" ",end=" ")
        
    for j in range(1,i+1):
        print((j+i)-1 , end=" ")
        

    for j in range(i+i-2,i-1,-1):
       
        print (j,end=" ")
       
       
    print()