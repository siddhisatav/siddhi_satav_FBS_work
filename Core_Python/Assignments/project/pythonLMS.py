import datetime
import os

class LMS :
    '''this class is used to keep record of books library
    it has total four module "display books " , "issue books","return book","add book"'''
    
    def __init__(self,list_of_books,library_name):
        self.list_of_books = "C:/Users/Admin/OneDrive/Desktop/FBS/Core_Python/project/list_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        Id = 101 
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content :
           self.books_dict.update({str(Id):{"books_title" : line.replace("\n" ,""),"lender_name":"","Issue_data": "","Status":"Available"}})
           Id=Id+1
            
            
    def display_books(self):
      print("--------------------------List of Books---------------------------")
      print("Books ID" , "\t", "Title")
      print("-------------------------------------------------")
      for key , value in self.books_dict.items():        
        print(key,"\t\t",value.get("books_title"),"- [",value.get("Status"),"]")   
    
    def Issue_books(self):
        
        
        
        
l=LMS("list_of_books.txt" , "pyhton's Library")
print(l.display_books())