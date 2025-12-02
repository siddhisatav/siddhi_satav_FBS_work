# 2. Python Program to Remove the nth Index Character from a Non-Empty
# String


def removeChar(str,n):
    return str[:n] + str[n+1:]

str = input("enter your string : ")
n = int(input("enter index of character to remove : "))
result = removeChar(str,n)
print(result)
    