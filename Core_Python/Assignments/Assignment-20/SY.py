# Write a program to
# 1. create a package “SY” which has class SYMARKS (Computer Total,
# MathsTotal, ElectronicsTotal).

class SYMARKS:
    def __init__(self, computer_total, maths_total, electronics_total):
        self.ComputerTotal = computer_total
        self.MathsTotal = maths_total
        self.ElectronicsTotal = electronics_total

    def display(self):
        print("Computer Total:", self.ComputerTotal)
        print("Maths Total:", self.MathsTotal)
        print("Electronics Total:", self.ElectronicsTotal)
