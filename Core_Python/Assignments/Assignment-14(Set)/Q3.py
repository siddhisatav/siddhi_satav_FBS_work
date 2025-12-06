# 3. Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.

def uniqueEle(li):

    dict1 = {}
    set1 = set(li)
    for i in li :
        
        if i in dict1: 
            dict1[i] += 1
            
        else :
            dict1[i] = 1
    
            
    return dict1 , set1 
        
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
ans = uniqueEle(words)
print("count of each element : ", ans[0])
print("Unique element : ", ans[1])
