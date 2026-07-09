class Student :
    def setData(self ,studid , name,dept):
         self.sid=studid
         self.sname = name
         self.dept=dept
         
    def getData(self):
          print("id:", self.sid)
          print("name :", self.sname)
          
obj1 = Student()
obj1.setData(1,"siddhi" , "cs")
obj1.getData()