# 12. Write a program to create three lists of numbers, their squares
# and cubes


def fun(li):
    square = []
    cube = []
    for i in range (len(li)):
        cube.append(li[i]*li[i]*li[i])
        square.append(li[i]**2)
    return cube , square 

li = [ 2,3,5,4,6,7]
result = fun(li)
print("list of numbers :",li)
print("Cube of numbers in list : ",result[0])
print("Square of numbers in list : ",result[1])
        