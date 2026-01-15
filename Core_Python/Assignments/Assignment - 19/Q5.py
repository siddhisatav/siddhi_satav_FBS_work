# 5. Find all of the words in a string that are less than 5 letters (take
# input from user)


strr = input("enter string : ")
words = strr.split(" ")
print(words)

li = [i for i in words if len(i) < 5 ]
print(li)