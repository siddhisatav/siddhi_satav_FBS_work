class calculator :
    def __init__(self,num1,num2,op):
        self.num1=num1
        self.num2=num2
        self.op=op
      
    
    
    def addition(self):
        add= self.num1+self.num2
        return f"Addition : {add}"
    
    def substraction(self):
        sub= self.num1-self.num2
        return f"substraction: {sub}"
    
    def multiply(self):
        mul= self.num1*self.num2
        return f"Multiplication: {mul}"
    
    def divide(self):
        div= self.num1/self.num2
        return f"division: {div}"
    
   
    
try:  
    
    num1 = int(input("enter num1 : "))
    num2 = int(input("enter num2 : ")) 
    op = input("enter operator : ")
    c1 = calculator(num1,num2,op)
    if op == "+":
      print( c1.addition())
    
    elif op == "-":
       print( c1.substraction())
   
    elif op == "*":
      print( c1.multiply())

    elif op == "/":
      print( c1.divide())
      
    else:
        raise ValueError("Invalid operator entered")


       
except ValueError as e :
        print("Error:" , e)
        
except ZeroDivisionError as e:
        print("Error : ", e)
        
except Exception :
          print("Error: Invalid number entered")
            
        