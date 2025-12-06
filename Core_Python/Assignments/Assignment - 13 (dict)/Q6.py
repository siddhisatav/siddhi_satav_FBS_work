# 6. Python Program to Multiply All the Items in a Dictionary

def multiplyItems(dict):
    
    res =1
    for key , value in dict.items():
        res *=value
      
        
    return res

dict ={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
print(dict)
ans = multiplyItems(dict)
print(ans)