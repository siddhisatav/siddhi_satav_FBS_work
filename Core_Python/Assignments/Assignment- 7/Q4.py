for i in range(1,6):
    
    
    print(" "*(6-i),end= " ")
    for j in range (1,i+1):
        if i==j or j==1 or i==5:
          print(j,end=" ")
        else:
            print(" ",end= " ")
    print()