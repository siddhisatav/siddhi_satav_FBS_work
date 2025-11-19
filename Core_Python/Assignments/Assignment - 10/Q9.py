# 9. Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.



def evenOdd(li):
    even_li=[0]*len(li)
    odd_li=[0]*len(li)
    e=0
    o=0
    for i in range (len(li)):
        if li[i] % 2 == 0:
            even_li[e] = li[i]
            e+=1
            
            
        else :
            odd_li[o] = li[i]
            o+=1
            
    return even_li , odd_li


li=[4,76,44,55,2,5]
print(li)
result = evenOdd(li)
print("Even list :",result[0])
print("Odd list :",result[1])
    