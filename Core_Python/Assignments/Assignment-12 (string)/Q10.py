# 10.Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions

def largesString(str1,str2):
    count1 = 0
    count2 = 0 
    for i in str1:
        count1 +=1
      
        
    for j in str2 :
        count2 +=1
      
    return count1 , count2

str1 =input("enter string1 : ")
str2 =input("enter string2 : ")
ans= largesString(str1 ,str2)
if ans[0] > ans[1]:
    print("Largest string is string1 \n Size of string1 is :", ans[0])
    
else:
    print("Largest string is string2 \n Size of string2 is :", ans[1])
