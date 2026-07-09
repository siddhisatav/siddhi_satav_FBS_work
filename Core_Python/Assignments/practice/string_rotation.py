def str_rotate(str):
    temp = str+str
    ans=""
    for i in range(len(str)):
        for j in range(len(str)):
            if i==len(str)-1 :
             ans+=temp[i+j]
    return ans

str = "ABCD"
print(str_rotate(str))