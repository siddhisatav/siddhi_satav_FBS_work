# 7. Python Program to Calculate the Length of a String Without Using a
# Library Function

def length(str):
    l = 0 
    for i in str : 
        l +=1
    return l 

str = input("enter string : ")
ans = length(str)
print(ans)