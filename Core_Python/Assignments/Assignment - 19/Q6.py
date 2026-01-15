# 6. Use a dictionary comprehension to count the length of each word
# # in a sentence (take input from user)



strr = input("enter string : ")
words = strr.split()
print(words)

di = {i : len(i) for i in words }
print(di)