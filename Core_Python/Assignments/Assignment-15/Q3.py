class Shirt:
    def __init__(self,sid="None",sname="None",type="None",price="None",size="None"):
        self.sid =sid   
        self.sname = sname
        self.type=type
        self.price = price
        self.size = size
        
        
    def showData(self):
        data=f"sid : {self.sid}\n sname = {self.sname}\ntype = {self.type}\n size={self.size}\n QUANTITY={self.price}"
        return data
        
          
    def showData(self):
        data = f"sid : {self.sid}\nsname{self.sname}\nprice{self.price}\nquantity{self.price}"
        return data
        
    def __del__(self):
        print("product record deleted !!")
        
c1 =Shirt(1,"soap",40,2)
print(c1.showData())
