class ComplexNumber :
    def __init__(self,real=0 , imag = 0):
        self.real =real
        self.imag=imag
        
    def __del__(self):
        pass
    
    def __add__(self , other):
        r = self.real + other.real
        i=self.imag + other.imag
        return f"{r}+{i}i"
        
    def __sub__(self,other):
        r = self.real - other.real
        i = self.imag - other.imag
        
        
        return f"{r}+{i}i"
    
        
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)



print("Sum: ",c1+c2)
print("Difference :",c1-c2)
