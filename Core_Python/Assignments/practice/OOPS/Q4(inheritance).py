class vehicle:
    def __init__(self,name , price,brand):
        self.name=name
        self.price=price
        self.brand=brand
        
    def getdata(self):
        print("name : " , self.name)
        print("name : " , self.price)
        print("name : " , self.brand)
        
class car(vehicle):
    def __init__(self,n,p,b,sunroof):
        super().__init__(n,p,b)
        self.sunroof=sunroof
    def getData(self):
        super().getdata()
        print("sunroof :", self.sunroof )
 
c1=car("bmw",100000,"black","ava")
c1.getData()   
print("brand",c1.name)