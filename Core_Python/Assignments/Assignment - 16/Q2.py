# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.


class Product:
    discount = 5/100
    def __init__(self , pid , pname,price,quantity):
        self.pid = pid 
        self.pname = pname 
        self.price = price 
        self.quantity =quantity
    
    def showBook (self):
        data = f"Product name = {self.pname}\npid = {self.pid}\nprice= {self.price}\nquantity={self.quantity}"
        return data
    
    
    def totalstudent(self):
        discountamount =(Product.discount ) * self.price 
        return self.price - discountamount
    def __del__(self):
        print("destructor is called ")
        
        
c1 = Product(1,"soap",50,2)
print(c1.showBook())
print(c1.totalstudent())

