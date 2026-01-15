# 3. Count the number of spaces in a string (take input from user)

s= input("enter any string :")
li = sum([1 for i in s if i  == " "  ])
print(li)