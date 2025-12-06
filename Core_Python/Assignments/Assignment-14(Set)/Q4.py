# 4. Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.

def findPairs(li,target):
    ans = []
    n = len(li)
    for i in range (n):
        for j in range (i+1 , n):
            if li[i] + li[j] == target:
                ans.append((li[i],li[j]))
                
    return ans
               
            
            
            
numbers = [1, 5, 7, -1, 5]
target = 6

result = findPairs(numbers, target)
print("Pairs with sum", target, ":", result)
    