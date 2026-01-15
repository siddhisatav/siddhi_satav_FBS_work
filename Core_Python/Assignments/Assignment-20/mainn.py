from TY import TYMARKS
from SY import SYMARKS

from TY import TYMARKS
from SY import SYMARKS

class Student:
    def __init__(self, rollno, name, sy_marks, ty_marks):
        self.rollno = rollno
        self.name = name
        self.sy_marks = sy_marks
        self.ty_marks = ty_marks

    def calculateGrade(self):
        total = self.sy_marks.ComputerTotal + self.ty_marks.Theory

        if total >= 70:
            return "A"
        elif total >= 60:
            return "B"
        elif total >= 50:
            return "C"
        elif total >= 40:
            return "Pass Class"
        else:
            return "Fail"

    def display_result(self):
        total = self.sy_marks.ComputerTotal + self.ty_marks.Theory
        grade = self.calculateGrade()

        print("----- Student Result -----")
        print("Roll No :", self.rollno)
        print("Name    :", self.name)
        print("SY Computer Marks :", self.sy_marks.ComputerTotal)
        print("TY Theory Marks   :", self.ty_marks.Theory)
        print("Total Marks       :", total)
        print("Grade             :", grade)


# ----- Main Program -----
sy = SYMARKS(45, 60, 55)
ty = TYMARKS(30, 25)

student = Student(1, "Rahul", sy, ty)
student.display_result()
