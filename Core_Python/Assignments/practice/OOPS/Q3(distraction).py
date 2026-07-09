class cricketer:
    def __init__(self,name,age,role):
        self.name=name
        self.age=age
        self.role=role
        
    def getData(self):
        print("name :",self.name)
        print("role :" , self.role)
        
    def __del__(self):
        print("destructor is called ")
        
c1 = cricketer("sachine ",55,"batsman")
c1.getData()
del c1
c1.getdata()