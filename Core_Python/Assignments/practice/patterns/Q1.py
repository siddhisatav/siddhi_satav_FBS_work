for i in range(1,6):
    for j in range(1,6):
        print("*",end= "")
    print()
    
print("****************************")


for i in range (1,6):
    for j in range(6-i,6):
        print(j ,  end = " ")
    print()
    
print("****************************")

for i in range ( 1, 6):
    for j in range(1,1+i):
        print(chr(64+j), end= " ")
    print()

print("****************************")

for i in range ( 1, 6):
    for j in range (1,1+i):
        print((i+j)-1,end= " ")
    print()

print("****************************")

for i in range (1,6):
    for j in range(1,(6-i)+1):
        print(j , end= " ")
    print()
    
print("****************************")

for i in range (1,6):
    n = i 
    for j in range(1,(6-i)+1):
        print(chr((64+n)) , end = " ")
        n+=1
    print()

print("****************************")

for i in range (1, 6):
    for j in range(1,6):
        if j==1 or j==5 or i==1 or i==5:
            print("*" , end= " ")
        else:
            print(" ", end= " ")
            
    print()
    
    
print("****************************")

for i in range (1,6):
    for j in range ( 1,6):
        if j==1 or i == 5 or i == j :
            print("*" , end= " ")
        else:
            print(" " , end = " ")
    print()
    
    
for i in range (1,6):
    n=i
    for j in range(i,6):
        print(j,end=" " ) 
      
    print()      
    
    
for i in range (1,6):
    for j in range(i,6):
        if i==1 or j==5 or  i == j :
            print(j,end=" ")
            
        else:
            print(" " , end= " ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print("*" , end=" ")
    print()
for i in range(1,5):
    for j in range (1,6-i):
        print("*",end=" ")
    print()
    
    
for i in range(1,6):
    for j in range(i,6):
        print(chr(64+j) , end= " ")
        
    print()
    