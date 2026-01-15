class Book :
    count = 0
    def __init__(self,bid=None,bname=None,author=None):
        Book.count +=1
        self.bid = bid 
        self.bname = bname
        self.author = author
        
    def showBook (self):
        data = f"book name = {self.bname}\nbook id = {self.bid}\nAuthor = {self.author}"
        return data
    
         
    def __del__(self):
        print("destructor is called ")
        
c1 = Book(1,"wings of fire","APJ Abdul kalam")
c2 = Book(2,"Abc" , "xyz")
print("count" , Book.count)
print(c1.showBook())
        
        

        
        