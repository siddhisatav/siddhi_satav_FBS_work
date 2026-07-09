# A=[1,2,3,2,3,6,7]

# a1=set(A)
# print(a1)
# for i in range(len(A)):
#     for j in range(i+1 , len(A)-1):
#         if A[i] == A[j]:
#             A.pop(j)
#             break
            
# print(A)

a={1:22,2:33,3:44,4:22}
dict={}

for key, value in a.items():
    if value not in dict.values():
        dict[key] = value
print(dict)
