def booking_possible(arr,dpar,k):
    task=[]
    for i in range(0,len(arr)):
        arr_tu =()
        arr_tu = arr_tu + (arr[i] , "RED")
        
        task.append(arr_tu)
    
    
    for i in range(0,len(dpar)):
        dept_tu = ()
        dept_tu =dept_tu +  (dpar[i] , "blue")
        task.append(dept_tu)
        
    
    task =sorted(task)
    print(task)
    guest = 0
    
    for e in task:
        if (task[1] == "RED"):
              guest = guest + 1
            
        elif(task[1] == "blue"):
             guest = guest - 1
            
        if (guest < k):
              print( "hi", 0) 
        else:
             print("hello" , 1)
        
    


    



arr=[1,3,5]
dpar=[2,6,8]
k=1
ans=booking_possible(arr,dpar,k)
print(ans)
        