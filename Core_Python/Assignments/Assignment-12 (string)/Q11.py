# 11. Python Program to replace every blank space with hyphen in a string.

def replaceBlankspace(str):
    str2 = ""
    for i in str:
        if i == " ":
            str2 += "-"
            
        else : 
            str2 += i
            
    return str2

str = input("enter string : ")
ans = replaceBlankspace(str)
print(ans)