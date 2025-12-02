# 6. Python Program to Take in a String and Replace Every Blank Space
# with Hyphen


def replaceStr(str):
    return str.replace(" ","-")
    

    
str= input("enter string : ")
ans = replaceStr(str)
print("Modified String :", ans)