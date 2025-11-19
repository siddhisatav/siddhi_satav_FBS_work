# 13 . Write a program to print list after removing even numbers.

def removeEven(li):
    ans=[]
    for i in range(len(li)):
        if li[i] % 2 != 0:
            ans.append(li[i])
            
    return ans

li=[2,33,4,5,67,7,9,8]
result= removeEven(li)
print("List before removing even numbers:",li)
print("List of Odd numbers: ",result)
            
            