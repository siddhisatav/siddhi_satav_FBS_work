# 2. Write a Python program to remove the intersection of a second set
# with a first set.

def removeintersection(A,B):
    set1=set()
    for i in A :
        if i not in B : 
            set1.add(i)
            
    return set1
            
        
  

   
A = {1, 2, 3, 4, 5}
B = {3, 4, 6}
ans = removeintersection(A,B)
print("First set after removing intersection:", ans)
    
        