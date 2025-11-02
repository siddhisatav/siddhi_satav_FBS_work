# G.

for i in range (1,6):
    n=i
    for j in range (1,7-i):
        print(" " , end= " ")
        
    for j in range ( 1, i+1):
        print(chr(64+j),end=" ")
        
    for j in range ( 1,i):
        print(chr(65+n),end=" ")
        n+=1
        
    print()