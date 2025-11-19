# 1. Python Program to Put Even and Odd elements of a List into two Different
# Lists

def seperateList(li):
    even=[]
    odd=[]
    for i in range (len(li)):
        if li[i] % 2 == 0 :
            even.append(li[i])
            
        else :
            odd.append(li[i])
            
    return even,odd 

li = [ 3,4,5,2,66,7,54]
print("Before separation : ", li)
result = seperateList(li)
print("list of even number : ", result[0])
print("list of odd number : ", result[1])
