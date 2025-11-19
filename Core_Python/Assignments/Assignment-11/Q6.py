# 6. Python Program to Find the Union of two Lists


def union(a,b):
    li=[]
    for i in a+b:
        if i not in li:
            li.append(i)

    return li






a = [1, 2, 3]
b = [3, 4, 5]
print("list a :", a)
print("list b :", b )
ans = union(a,b)
print("Union of lists : ", ans )

