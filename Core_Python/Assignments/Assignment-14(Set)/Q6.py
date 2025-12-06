# 6. Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.

def product(li):
    n=len(li)
    ans=[]
    pro = 0
    for i in range(1,n):
        
        for j in range(i+1,n):
            if li[i] * li[j] > pro :
                pro = li[i] * li[j]
                ans=(li[i],li[j])
                
                
    return ans , pro

numbers = [1, 5, 7, -1, 5]


result = product(numbers)
print("Pair with maximum product:", result[0])
print("Maximum product:", result[1])
                
        
                