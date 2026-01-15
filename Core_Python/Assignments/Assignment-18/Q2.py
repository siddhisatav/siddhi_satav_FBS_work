# 2. Create a class Distance with data members as km,m and cm and add following
# methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class Distance : 
    def __init__(self,km,m,cm):
        self.km=km
        self.m=m
        self.cm=cm
        self.convert()
        
    def convert(self):
        # convert cm to m 
        self.m += self.cm // 100
        self.cm = self.cm % 100

        # Convert m to km
        self.km += self.m // 1000
        self.m = self.m % 1000
        
        
        
    
    def __add__(self ,other):
        
       ans = Distance( 
        self.km + other.km,
         self.m + other.m,
        self.cm + other.cm)
       return ans
       
       
   
    def __sub__(self,other):
        ans = Distance( 
        self.km - other.km,
        self.m - other.m,
        self.cm - other.cm)
        return ans
    
    def display(self):
        print(f"{self.km} km {self.m} m {self.cm} cm")

       
c1 = Distance(2, 500, 80)
c2 = Distance(1, 750, 50)

print("Sum:", end=" ")
(c1 + c2).display()

print("Difference:", end=" ")
(c1 - c2).display()

   
        