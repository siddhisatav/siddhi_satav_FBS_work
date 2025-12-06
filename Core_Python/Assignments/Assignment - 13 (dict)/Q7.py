# 7. Python Program to Remove the Given Key from a Dictionary

def RemoveKey(dict , k ):
    dict2 = {}
    for key , value in dict.items():
        if key != k :
            dict2[key] = value
            
    return dict2

dict={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
k = int(input("enter key : "))

ans = RemoveKey(dict , k )
print(ans)    