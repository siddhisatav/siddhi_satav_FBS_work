class Product:
    def __init__(self,pid="None",pname="None",price="None",quantity="None"):
        self.pid=pid
        self.pname=pname
        self.price =price
        self.quantity = quantity
        
    def showData(self):
        data = f"pid : {self.pid}\npname{self.pname}\nprice{self.price}\nquantity{self.quantity}"
        return data
        
    def __del__(self):
        print("product record deleted !!")
        
c1 = Product(1,"soap",40,2)
print(c1.showData())
