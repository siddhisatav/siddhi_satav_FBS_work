# 7. Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.

def missing(set1,set2):
    set3=set()
    set4=set()
    for i in set1:
        if i not in set2:
             set3.add(i)
    for j in set2 :
        if j not in set1 :
            set4.add(j)
                
    return set3,set4

A = {1, 2, 3, 4, 5}
B = {3, 4, 6}
ans = missing(A,B)
print("missing numbers in the second set as compared to the first",ans[0])
print("missing numbers in the first set as compared to the second ", ans[1])
                