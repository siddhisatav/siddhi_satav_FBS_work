# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.


class Shirt:
    shirtPrice = 0 
    def __init__(self,sid , sname ,type,price , size):
        self.sid = sid 
        self.sname=sname
        self.type = type 
        self.price=price
        self.size =size
        
    def show(self):
        data = f"\nsid ={self.sid}\nsname = {self.sname}\ntype = {self.type}\nActual price = {self.price}Rs\nsize = {self.size} "
        return data
    
    def __del__(self):
          print("destructor is called ")
          
    def sizePrice(self):
            if self.size == "small":
        
                Shirt.shirtPrice =self.price
                
            elif self.size == "medium":
                s = (0.1*self.price)
                Shirt.shirtPrice= s + self.price
                
            elif self.size == "large":
                l= s * 2 
                Shirt.shirtPrice = l+self.price
                
            return Shirt.shirtPrice

c1 = Shirt(1,"plain white","Formal",2000,"medium")   
print("shirt price according to size : ",c1.sizePrice(),"Rs")
print("\n****Shirt details****\n",c1.show())
         
        
        
