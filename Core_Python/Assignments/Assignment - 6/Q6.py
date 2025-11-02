# F.

for i in range (1, 6):
    for j in range(1,7-i):
        print(" ", end=" ")
        
    for j in range(1,i+1):
        print(j,end= " ")
        n=i
    for j in range (1,i):
        print(n+1,end=" ")
        n+=1
    print()