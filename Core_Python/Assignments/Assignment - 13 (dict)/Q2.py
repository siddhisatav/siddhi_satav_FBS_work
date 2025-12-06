# 2. Python Program to Concatenate Two Dictionaries Into One

def concatDict(dict1,dict2):
    dict3={}
    for d in (dict1,dict2):
        for key , value in d.items():
         dict3[key] = value
    return dict3

dict1 = {'name': 'siddhi','age':'21'}
dict2={'course' : 'python'}
ans = concatDict(dict1,dict2)
print(ans)