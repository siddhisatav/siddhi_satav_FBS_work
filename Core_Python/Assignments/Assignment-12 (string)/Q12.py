# 12. Python Program to count number of lowercase characters in a string.

def countLowerCase(str):
    count = 0 
    for i in str :
        if i >= 'a' and i<='z':
            count+=1
            
    return count

str = input("Enter a string: ")
lower_count = countLowerCase(str)

print("Number of lowercase characters:", lower_count)