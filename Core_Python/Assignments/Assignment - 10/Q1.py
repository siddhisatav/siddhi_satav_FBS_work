# 1. Write a program to find sum of all elements of list


def sumList(li):
    sum =0
    for i in range (0,len(li)):
        sum = sum+li[i]
        
    return sum

li = [2,3,4,5]
result= sumList(li)
print(result)