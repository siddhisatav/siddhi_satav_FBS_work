# 2. Python Program to Merge Two Lists and Sort it

def merge(li1,li2):
    ans=[]
    i=0
    j=0
    for i in range(len(li1)):
        ans.append(li1[i])

    # copy li2 to ans
    for j in range(len(li2)):
        ans.append(li2[j])
                
    return ans 
    
        
def sortEle(ans):
    size = len(ans)
    for i in range(1,size):
        for j in range (0,size-i):
            if ans[j] > ans[j+1]:
                ans[j],ans[j+1]=ans[j+1],ans[j]
                
    return ans
    


li1=[2,3,53,3,70,55]
li2=[33,70,66,43,20]
print("list1 :" , li1)
print("List2 : ", li2)
result1=merge(li1,li2)
result2 = sortEle(result1)
print(result2)
        