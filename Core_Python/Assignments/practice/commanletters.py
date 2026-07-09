# str1 ="naina"
# str2="reene"
# str3=set(str1)
# str4 =set(str2)
# print(str3 & str4)

# strr="sheena loves eating apple and mango. her sister also loves eating apple and mango"

# word = strr.split()
# count={}

# for i in word:
#     if i in count :
#         count[i] +=1
        
#     else:
#         count[i] = 1
        

# print(count)



# list1=["naina","kimi","shenna"]
# list2=[7238,293,3329,2198]
# dictt={}
# for i in range(len(list1)):
#    dictt[list2[i]] = list1[i]
# print(dictt)    

# arr=[1,2,3,5,6,7]
# n=len(arr)
# print(n+2)

# for i in range(len(arr)+2):
#     total_sum+=i
# print(total_sum)   
# actual_sum=0
# for i in arr:
#     actual_sum+=i
# print(actual_sum)
# print(total_sum-actual_sum )   

# arr=[5,7,4,3,9,8,19,21,12]
# sum=17
# summ=[]
# for i in range(0,len(arr)):
#     for j in range(i+1):
#         if arr[i]+arr[j] == 17:
#             print(arr[i],arr[j])
            
       
class Node:
    def __init__(self , key):
        self.data = key
        self.left = None
        self.right = None
        
def height_tree(A):
        if(A==None):
            return 0 
        else:
            ldepth = height_tree(A.left)
            rdepth = height_tree(A.right)
            
        if (ldepth > rdepth):
            return(1+ldepth)
        else:
            return(1+rdepth)
        

root =Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left =Node(4)
root.left.right = Node(5)
root.left.left.left=Node(7)
root.right.right = Node(6)

print(height_tree(root))