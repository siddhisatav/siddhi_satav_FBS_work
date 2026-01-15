# 4. Remove all of the vowels in a string (take input from user)

strr = input("enter string : ")
vowel = ['a','e','i','o','u']
li =''.join([ch for ch in strr if ch not in vowel])

print(li)