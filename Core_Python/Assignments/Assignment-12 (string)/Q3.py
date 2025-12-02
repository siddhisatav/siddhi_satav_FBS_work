# 3. Python Program to Detect if Two Strings are Anagrams
def Anagrams(str1,str2):
    for i in str1 :
        count1 = 0
        count2 = 0 
        for x in str1 :
            if x == i :
                count1 +=1
        for y in str2:
            if y == i :
                count2 +=1
        if count1 != count2 :
            return False
    
    return True
            
            
            
str1 = input("enter string1 : ")
str2 = input("enter str2 : ")
ans =Anagrams(str1,str2)
print(ans) 
        