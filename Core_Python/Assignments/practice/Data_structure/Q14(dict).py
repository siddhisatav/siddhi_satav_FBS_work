dict = {1:"python" , 2: "java" ,3: "c++","a" : 123}
print(dict)
dict2=dict.copy() #make a copy of dict
print(dict2) 
dict.clear() #clear dict 
print(dict)

print(dict2.get(4,'key not found')) #getting the value of the 4th key if not found then print "key not found"

print(dict2.items()) # print items of the list 
print(dict2.keys())  #print keys of the dict
print(dict2.pop(3))  #pop given key from the dict 
print(dict2)          
dict2.popitem()       #remove last element from dict
print(dict2)
dict2.update({4:'d',5:"a"})  #update element 
print(dict2)
print(dict2.values())  #print values from the dict
print(dict2.get(4,'key not found')) 
print(dict2)