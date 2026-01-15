
# 1. Create a class Student with following
# a. data members :
# i. StudentId
# ii. Name
# iii. Age
# iv. Percentage
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. Method CalculateRank
# v. Override __str__ Method








class Student :
    def __init__(self,studentId , name,age,Percentage):
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
    
    
c1 =Student(1,"siddhi" , 21,81,)

print(c1.display())
print()
print(c1.calculateRank())
print()
print(c1)

                            
    
    
    