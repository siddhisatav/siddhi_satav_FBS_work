class television :
     def __init__(self):
        self.model_no = 0
        self.screen_size = 0
        self.price = 0
        
     def accept(self):
         try :
             self.model_no = int(input("enter model number : "))
             if self.model_no > 9999 :
                 raise ValueError("model number should not exceed 4 digits")
             
             self.screen_size = int(input("enter screen size : "))
             
             if self.screen_size < 12 or self.screen_size > 70 :
                     raise ValueError("Screen size must be between 12 and 70 inches")

             self.price = int(input("Enter price: "))
             if self.price < 0 or self.price > 5000:
                raise ValueError("Price must be between 0 and 5000 Rs")
                 
                 
         except Exception as e :
             print("Exception caught : " , e)
             
             self.model_no = 0
             self.screen_size = 0
             self.price=0
             
             
     def display(self):
         print("\nTelevision Details")
         print("Model Number :", self.model_no)
         print("Screen Size  :", self.screen_size)
         print("Price        :", self.price)
         
    
tv = television()
tv.accept()
tv.display()

         
    