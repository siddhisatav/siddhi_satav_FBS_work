# t1 = (1,2,3)
# t1 = (1,2,3,4)
# print(t1)


# print(type(t1))

# li=[1,2,3,4]
# li=[1,2,3]
# print(li)




def sortt(t1):
    t1 =list(t1)
    size = len(t1)
    for i in range(1,size):
        for j in range(0,size-i):
            if t1[j] > t1[j+1]:
                t1[j],t1[j+1] = t1[j+1],t1[j]
                
    return tuple(t1)

t1 = (1,4,5,6,3,8)
ans=sortt(t1)
print(ans)

print("min element : ",t1[0])
print("max element :" , t1[-1])
print(t1.count(4))

count=0
for i in t1:
    count +=1
    
    
print(count)

t2=(1,2,3)
ans=t1+t2
print(ans)


