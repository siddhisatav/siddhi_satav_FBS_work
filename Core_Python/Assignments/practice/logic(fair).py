import functools


stops=["sh","d","s","kn","w","kd"]
fare=[50,25,15,20,10,12]

so="kd"
des = "d"
price=[]


for i in range(len(stops)):
    if stops[i] == so:
        start = i 
        
    if stops[i]==des:
        end = i
        
        
if start < end:

     for i in range (start+1 ,end+1):
  
         price.append(fare[i])
         
if start > end :
    for i in range(end+1,start+1):
        price.append(fare[i])
        
     
    
         

             
total = sum(price)

        
        
        
print("route: ",so ,"to", des)
print("fair : " , total)