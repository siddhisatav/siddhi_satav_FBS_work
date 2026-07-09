
import os 
from datetime import datetime , timedelta
from tabulate import tabulate
import pwinput

class Library:
    def __init__(self):
        self.Book_file ="C:/Users/Admin/OneDrive/Desktop/FBS/Core_Python/project/books.txt"
        self.member_file = "C:/Users/Admin/OneDrive/Desktop/FBS/Core_Python/project/member.txt"
        self.issue_file = "C:/Users/Admin/OneDrive/Desktop/FBS/Core_Python/project/issues.txt"
        self.admin_password = "admin"
        self.member_password = "member"
        self.setup_files()
        
        
    def setup_files(self):
        for f in[self.Book_file , self.issue_file]:
            if not os.path.exists(f):
                open(f,"w").close()
     
     
     
    def check_admin(self):
        password = pwinput.pwinput("Enter your admin password: ", mask="*")
        if password != self.admin_password:
            print("Wrong password! Acess denied.")
            return False
        
        return True
    
    def check_memberss(self):
        password = pwinput.pwinput("enter your member password : ")
        if password != self.member_password:
            print("Wrong password! Acess denied.")
            return False
        
        return True


    def add_book(self):
         if not self.check_admin(): return
         
         while True :
              bid =  input("Book ID : ")
              title = input("Title : ")
              bookdata=[]
              found = False
              with open(self.Book_file,"r") as fb:
                  for line in fb :
                      if not line.strip():
                          continue
                      p = line.strip().split("|")
                      bookdata.append(p)
                      
              duplicate_found = False
            
              for i in bookdata:
                  if i[0] == bid :
                     print("Book ID already exists . try again.")
                     duplicate_found = True
                     break
                 
                  
             
                  if i[1].lower() == title.lower():
                      print("Book Title already exists,try again . ")
                      duplicate_found = True
                      break
                  
              if duplicate_found:
                   continue   
              break
                    
         
         qty=input("Quantity : ")  
         author = input("Author : ")
         with open(self.Book_file,"a") as fp:
            
             fp.write(f"{bid}|{title}|{author}|{qty}\n")
         print("------------Book Added----------\n")
        
        
    def view_book(self):
        try:
             with open(self.Book_file,"r")as fr:
                 books = [line.strip().split("|")for line in fr if line.strip()]
            
        except FileNotFoundError:
              print("Books file not found!")
              return
        except Exception as e:
              print("Error reading books:", e)
              return
            
        if not books:
            print("no books found")
            return 
        
        books.sort()
        headers = ["Book ID", "Title", "Author", "Available Qty"]
        print(tabulate(books, headers=headers, tablefmt="grid"))
            
            
            
            
    def is_book_issued(self, bid):
         with open(self.issue_file, "r") as f:
              for line in f:
                 if not line.strip():
                     continue
                 p = line.strip().split("|")
           
                 if p[1] == bid and p[5].lower() == "issued":
                     return True
         return False

            
            
    def delete_book(self):
        if not self.check_admin(): return

        bid = input("Book ID to delete : ")
        
        # chech issue status
        
        if self.is_book_issued(bid):
             print("Cannot delete book.")
             print("Book is currently issued to a member.")
             return
        
        
        # Delete Book

        with open(self.Book_file,"r") as fr : 
            books = fr.readlines()
            
        new_books = [b for b in books if not b.startswith(bid+"|")]
        with open(self.Book_file,"w")as f:
            f.writelines(new_books)
            
        print("-------------Book Deleted--------------\n")
        
        
    def check_member(self, member_id):
       with open(self.member_file, "r") as f:
         for line in f:
            if not line.strip():
                continue
            p = line.strip().split("|")
            if p[0] == member_id:
                return True
         return False


    def issue_book(self):
       
        
        member_id =input("Enter your Id: ")
        bid = input("Book Id To Issue: ")
    

        if not self.check_member(member_id):
          print("You are not a registered member!!\nPlease enter your details")
          self.add_member()
          return
    
        
        
        with open(self.Book_file,"r")as fr:
            books=fr.readlines()
            
        for i in range(len(books)):
            p = books[i].strip().split("|")
            if p[0] == bid and int(p[3]) > 0 :
                p[3] = str(int(p[3]) - 1)
                books[i] = "|".join(p)+ "\n"
                with open(self.Book_file,"w") as f:
                    f.writelines(books)
                    
                issue_id = len(open(self.issue_file).readlines())+1
                issue_date = datetime.now().strftime("%Y-%m-%d")
                due_date = (datetime.now()+timedelta(days=14)).strftime("%Y-%m-%d")
                with open(self.issue_file,"a") as f :
                 
                    f.write(f"{issue_id}|{bid}|{member_id}|{issue_date}|{due_date}|issued\n\n")
                    
                print("-----Book Issued----")
                return
        print("book not available")
                

        
    def return_book(self):
  
          
        member_id = input("Enter your Id: ")

        if not self.check_member(member_id):
         print("You are not a registered member.")
         self.add_member()
         return
        
        iid = input("Issue ID to return : ")
        with open(self.issue_file,"r") as f :
            issues = f.readlines()
            
        with open(self.Book_file,"r") as f :
            books =f.readlines()
            
        for i in range(len(issues)):
            p =issues[i].strip().split("|")
            if p[0] == iid and p[2] == member_id and p[5] == "issued":
                p[5] ="returned"
                issues[i] = "|".join(p) +"\n"
                for j in range(len(books)):
                    bp =books[j].strip().split("|")
                    
                    if bp[0] == p[1]:
                        bp[3] = str(int(bp[3]) + 1)
                        books[j] = "|".join(bp) +"\n"
                        
                with open (self.issue_file,"w") as f:
                    f.writelines(issues)
                    
                with open(self.Book_file,"w") as f:
                    f.writelines(books)
                    
                print("------------Book Returned-------------\n")     
                
        print("-------Invaild Issue ID or member ID------\n")
        
                      
    def search_book(self):
        key = input("Enter Book ID : ")
        
        with open(self.Book_file,"r") as fr:
            books = fr.readlines()
            
        for i in books :
            p=i.strip().split("|")
            if p[0] == key or p[1] == key:
                print("--------Book Found------\n")
                print(tabulate([p],headers=["Book ID" , "Title" ,"Author","Qty"],tablefmt="grid"))
                
                return
        else:   
            print("------------Book Not Found------------\n ")
            print("1 - Enter the book id again or 2 - go to menu ")
            k=int(input("enter "))
            if k == 1 :
               self.search_book()
               
            else :
                self.main_menu()
                
            
           
            
                                                                      
    def issued_books(self):
        if not self.check_admin():return
        
        with open(self.issue_file,"r") as f :
            issues = f.readlines()
            
        print("\n---------Issued Books-----------\n")
        issue=[]
        for i in issues:
            p = i.strip().split("|")
            if len(p) >= 4 and p[-1] == "issued":  
                 issue.append(p)
                 
        header=["Issue ID","Book ID","Member ID","Issued Date","Status"]
        if issue:
             issue.sort()
             print(tabulate(issue,headers=header,tablefmt="grid"))
        else:
            print("No valid member records found !!")
            
                
                
    def available_books(self):
        data=[]
        with open(self.Book_file,"r") as f:
            dat = f.readlines()
            
        print("\n-----------Available Books-----------\n")
        for b in dat:
            p = b.strip().split("|")
            if int(p[3])> 0:
                  data.append(p)
                  
        header=["Book ID","Title","Author","Qty"]
        if data :
             data.sort()
             print(tabulate(data,headers=header,tablefmt="grid"))
        else:
            print("No valid member records found !!")
            
             
   
                    
                    
    def add_member(self):  
        # if not self.check_memberss():return 
        
        while True : 
             mid = input("Enter member id :")
             found = False
        
             with open(self.member_file,"r") as fb:
                 for line in fb :
                      if not line.strip():
                         continue
                      p = line.strip().split("|")
                      if p[0] == mid :
                          found = True
                          break
                       
             if found:
                 print("Member ID already exists. Try again.")
             else:
                 break
    

        name = input("Enter name :")
        phone = input("Enter phone number :")
        with open (self.member_file , "a") as f:
           
            f.write(f"{mid}|{name}|{phone}\n ")
            
        print ("----------------Member Added---------------\n-")
        
    
                    
                
    def view_members(self):
        with open(self.member_file,"r") as fr :
            members = fr.readlines()
            
        if not members:
            print("No member found")
        
        
        data = []
        header=["Member ID" , "Name" ,"Phone Number"]
        
    
        for m in members:
            p = m.strip().split("|")
            if len(p)==3:
                data.append(p)
                
        if data :
             data.sort()
             print(tabulate(data,headers=header,tablefmt="grid"))
        else:
            print("No valid member records found !!")
            
            
    def search_member(self):
        
        if not self.check_memberss():return 
        key = input("Enter member id :")
        
        with open(self.member_file,"r")as f:
            members = f.readlines()
            
        for m in members:
            p = m.strip().split("|")
            if(p[0] == key or  p[1] == (key)):
                print("-------------Member Found----------\n")
                print(tabulate([p],headers=["Book ID" , "Title" ,"Author","Qty"],tablefmt="grid"))
                return
                
              
             
        print("Member Not Found")
                   
        
    def delete_member(self):
        member_id = input("Enter your Id: ")

        if not self.check_member(member_id):
          print("You are not a registered member.")
          self.add_member()
          return

        mid = input("Enter Member Id To Delete : ")
        
        with open(self.member_file,"r")as f:
            members = f.readlines()
            
        new_members = []
        
        for i in members :
            p = i.strip().split("|")
            
            if len(p)!=3:
                continue
            if p[0] !=mid : 
                new_members.append(i)
            else:
                found = True
                
        if found :
            with open(self.member_file,"w")as fr :
                fr.writelines(new_members)
            print("---------------Member Deleted-----------\n")
            
        else:
            print("-------------Member Not Found-------------\n")
            
            
            
        

    def main_menu(self):
        while True:
          print("""
                 1.Book Menu
                 2.Member Menu
                 3.Issue Book
                 4.Return Book
                 5.Reports
                 6.Exit
                 """)
          try:
                ch= int(input("Enter your choice: "))
          except ValueError:
                print("Invalid input! Please enter a number.")
                continue
 

          if ch == 1: self.book_menu()
          elif ch == 2: self.member_menu()
          elif ch == 3: self.issue_book()
          elif ch == 4: self.return_book()
          elif ch == 5: self.report_menu()
          elif ch == 6: break

    def book_menu(self):
          while True:
             print("\n\n---------------Book Menu---------------\n\n")
             print("1.Add 2.View 3.Search 4.Delete 5.Back")
             
             try:
                c= input("Enter your choice: ")
             except ValueError:
                print("Invalid input! Please enter a number.")
                continue
             
             if c == "1": self.add_book()
             elif c == "2":self.view_book()
             elif c == "3": self.search_book()
             elif c == "4": self.delete_book()
             elif c == "5": break

    def member_menu(self):
         while True:
             print("\n\n--------------Member Menu---------------\n\n")
             print("1.Add 2.View 3.Search 4.Delete 5.Back")
             
             try:
                c= int(input("Enter your choice: "))
             except ValueError:
                print("Invalid input! Please enter a number.")
                continue
             
            
             if c == "1": self.add_member()
             elif c == "2": self.view_members()
             elif c == "3": self.search_member()
             elif c == "4": self.delete_member()
             elif c == "5": break

    def report_menu(self):
        
          print("\n\n---------------Report Menu---------------\n\n")
          print("1.Issued 2.Available ")
          
          try:
             c= int(input("Enter your choice: "))
          except ValueError:
              print("Invalid input! Please enter a number.")
              
            
          c = input("Choice : ")
          if c == "1": self.issued_books()
          elif c == "2":self. available_books()
         

# ---------- START ----------
if __name__ == "__main__":
    lib = Library()
    lib.main_menu()