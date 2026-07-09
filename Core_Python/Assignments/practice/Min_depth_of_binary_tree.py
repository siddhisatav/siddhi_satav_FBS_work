class node :
    def __init__(self,key):
        self.data= key
        self.left =None
        self.right=None
        
        
def min_depth(A):
    if(A==None):
        return 0 
    else :
        lDepth = min_depth(A.left)
        rDepth = min_depth(A.right)
        
    if (lDepth > rDepth):
        return (rDepth+1)
    else:
        return (lDepth+1)
            
        

root=node(1)
root.left=node(2)
root.left.left=node(4)
root.left.left.right=node(7)
root.left.right=node(5)
root.right=node(3)
root.right.right=node(6)

print(min_depth(root))