# 14. Python Program to count the occurrences of each word in a string.
def countOccurence(str):
    count = {}
    word= str.split()
    for i in word :
        if i not in count :
            count[i] = 1
            
        else:
            count[i]+=1
            
    return count
            
str = input("enter string: ")
ans = countOccurence(str)
print(ans)
            
        
    
