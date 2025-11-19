# 8. Write a program to create a duplicate of an existing list. It should not point to
# same list.



def duplicateList(li):
    new_li = []
    n=0
    for i in li:
        if i not in new_li:
            new_li.append(i)
        

    return new_li

li = [2,4,3,5,6,2,4]
print("original list : ", li)
result = duplicateList(li)
print("Duplicate list : ",result)