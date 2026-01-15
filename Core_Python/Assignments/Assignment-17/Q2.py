class Student :
    
    def __init__(self,studentId = None, name=None,age=None,Percentage=None):
        self.studentId = studentId
        self.name=name
        self.age=age
        self.Percentage = Percentage
    
    
    def Accept(self):
        self.studentId=int(input("enter student id : "))
        self.Name = input("Enter Name: ")
        self.Age = int(input("Enter Age: "))
        self.Percentage = float(input("Enter Percentage: "))
        
        
    
    def display(self):
        data = f"StudentID = {self.studentId}\nName = {self.name}\nname={self.age}\nage={self.age}\npercentage={self.Percentage}"
        return data
    
    def calculateRank (self):
        if self.Percentage >= 75:
            return "Distinction"
        elif self.Percentage >= 60:
            return "First Class"
        elif self.Percentage >= 50:
            return "Second Class"
        elif self.Percentage >= 40:
            return "Pass"
        else:
            return "Fail"
        
    def __str__(self):
        return (f"StudentID = {self.studentId}\nName = {self.name}\nname={self.age}\nage={self.age}\npercentage={self.Percentage}")
    
    
    
class EnggStudent(Student):
    def __init__(self, studentId=None, name=None, age=None, Percentage=None,branch =None, internalMarks=None):
        super().__init__(studentId, name, age, Percentage)
        self.branch =branch
        self.internalMarks=internalMarks
        
        
    def Accept(self):
        super().Accept()
        self.branch = input("enter branch : ")
        self.internalMarks =int(input("enter your makrs :"))
        
    def display(self):
        super().display()
        data = f"branch = {self.branch} \ninternalMarks= {self.internalMarks}"
        return data 
    
    def CalculateRank(self):
     
        total_score = (0.7 * self.Percentage ) + (0.3 * self.internalMarks)
        if total_score >= 75:
            return "Distinction"
        elif total_score >= 60:
            return "First Class"
        elif total_score >= 50:
            return "Second Class"
        elif total_score >= 40:
            return "Pass"
        else:
            return "Fail"
        
        
    def __str__(self):
        return (super().__str__() + 
                f", Branch: {self.branch}, Internal Marks: {self.internalMarks}")
    
c1 =EnggStudent()
c1.Accept()

print(c1.display())
print()
print(c1.calculateRank())
print()
print(c1)

                            
    
    
    
        