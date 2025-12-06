# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not

def checkKey(dict,k):
    for i in (dict):
      
        if i == k :
            return True
        else:
            return False
            
dict = {"a": 1, "b": 2,"c": 3, "d": 4}

k=input("enter key to search : ")
ans = checkKey(dict , k)
print(ans)