# 7. Python Program to Find the Intersection of Two Lists

def intersection(a,b):
    li=[]
    for i in a:
        if i in b and not i in li :
            li.append(i)

    return li

a= [1, 2, 3]
b = [3, 4, 5]
print("list a :", a)
print("list b :", b )
ans = intersection(a,b)
print("Intersection of lists : ", ans )
