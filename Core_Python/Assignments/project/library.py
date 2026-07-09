import os 
from datetime import datetime , timedelta
from tabulate import tabulate


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
        password = input("enter your admin password : ")
        if password != self.admin_password:
            print("Wrong password! Acess denied.")
            return False
        
        return True
    
    def check_member(self):
        password = input("enter your member password : ")
        if password != self.member_password:
            print("Wrong password! Acess denied.")
            return False
        
        return True


    def add_book(self):
         if not self.check_admin(): return
         bid =  input("Book ID : ")
         title = input("Title : ")
         author = input("Author : ")
         qty=input("Quantity: ")
    
         with open(self.Book_file,"a") as fp:
            
             fp.write(f"{bid}|{title}|{author}|{qty}\n")
         print("------------Book Added----------\n")
        
    def sortdata(self,data):
        size=len(data)
        for i in range(size):
            for j in range(0,size-i- 1):
                if data[j][0] > data[j+1][0]:
                    data[j],data[j+1]=data[j+1] ,data[j]
                return data 
            
    def view_book(self):
        with open(self.Book_file,"r")as fr:
            books = [line.strip()for line in fr if line.strip()]
            
        if not books:
            print("no books found")
            return 
        
            
        print("\nID\t\t|\t\tTitle\t\t|\t\tAuthor\t\t|\t\tAvl/Total\n")
        for b in books:
            p = b.split("|")
            print(f"{p[0]}\t\t|\t\t{p[1]}\t\t|\t\t{p[2]}\t\t|\t\t{p[3]}")
            
            
    def delete_book(self):
        if not self.check_admin(): return
        bid = input("Book ID to delete : ")
        with open(self.Book_file,"r") as fr : 
            books = fr.readlines()
            
        new_books = [b for b in books if not b.startswith(bid+"|")]
        with open(self.Book_file,"w")as f:
            f.writelines(new_books)
            
        print("-------------Book Deleted--------------\n")
        
        
    def issue_book(self):
        if not self.check_member(): return 
        
        member_id =input("Enter your Id: ")
        bid = input("Book Id To Issue: ")
        
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
        print("book bot available")
                

        
    def return_book(self):
        if not self.check_member():return
        
        member_id = input("enter yout ID : ")
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
            if p[0] == key :
                print("--------Book Found------\n")
                print(f"Book Id\t\t\t Book Name\t\t\t Book Author\t\t\t Qty\n\n")
                print(f"{p[0]}\t\t\t {p[1]}\t\t\t {p[2]}\t\t\t {p[3]}")
                
                return
                
            print("------------Book Not Found------------\n ")
            
                                                                      
    def issued_books(self):
        if not self.check_admin():return
        
        with open(self.issue_file,"r") as f :
            issues = f.readlines()
            
        print("\n---------Issued Books-----------\n")
        for i in issues:
            p = i.strip().split("|")
            if len(p) >= 5 and p[-1] == "issued":  
                print(f"Book Id\t\t\t Book Name\t\t\t Book Author\t\t\t Qty\n\n")
                print(f"{p[0]}\t\t\t {p[1]}\t\t\t {p[2]}\t\t\t {p[3]}")
                
                
    def available_books(self):
        with open(self.Book_file,"r") as f:
            data = f.readlines()
            
        print("\n-----------Available Books-----------\n")
        for b in data:
            p = b.strip().split("|")
            if int(p[3])> 0:
               print(f"Book Id\t\t\t Book Name\t\t\t Book Author\t\t\t Qty\n\n")
               print(f"{p[0]}\t\t\t {p[1]}\t\t\t {p[2]}\t\t\t {p[3]}")
                
                
    def overdue_books(self):
        if not self.check_admin():return 
        today = datetime.now()
        with open(self.issue_file,"r")as f:
            issues = f.readlines()
        print("\n-------------Overdue Books--------------\n")
        for i in issues:
            p = i.strip().split("|")
            
            if len(p) != 6:
              continue 
            
            if p[5] == "issued":
                due = datetime.strptime(p[4], "%Y-%m-%d")
                if today > due:
                    print(p, "Days Overdue:", (today - due).days)
                    
                    
    def add_member(self):  
        if not self.check_member():return 
        mid = input("Enter member id : ")
        name = input("Enter name :")
        phone = input("Enter phone number :  ")
        with open (self.member_file , "a") as f:
           
            f.write(f"{mid}|{name}|{phone}\n ")
            
        print ("----------------Member Added---------------\n-")
        
    def view_members(self):
        with open(self.member_file,"r") as fr :
            members = fr.readlines()
            
        if not members:
            print("no member found")
            
        print("\nID\t\t\t Name\t\t\t Phone")
        for m in members:
            p = m.strip().split("|")
            if len(p)!=3:
                continue
            print(f"{p[0]}\t\t\t {p[1]}\t\t\t {p[2]}")
            
            
    def search_member(self):
        
        if not self.check_member():return 
        key = input("Enter member id :")
        
        with open(self.member_file,"r")as f:
            members = f.readlines()
            
        for m in members:
            p = m.strip().split("|")
            if(p[0] == key ):
                print("-------------Member Found----------\n")
                print("\nID\t\t\t Name\t\t\t Phone\n")
                print(f"{p[0]}\t\t\t {p[1]}\t\t\t {p[2]}\n")
                
                
        print("Member Not Found")
                   
        
    def delete_member(self):
        if not self.check_member():return 
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
          ch = input("Choice: ")

          if ch == "1": self.book_menu()
          elif ch == "2": self.member_menu()
          elif ch == "3": self.issue_book()
          elif ch == "4": self.return_book()
          elif ch == "5": self.report_menu()
          elif ch == "6": break

    def book_menu(self):
          while True:
             print("---------------Book Menu---------------")
             print("1.Add 2.View 3.Search 4.Delete 5.Back")
             c = input("Choice: ")
             if c == "1": self.add_book()
             elif c == "2":self.view_book()
             elif c == "3": self.search_book()
             elif c == "4": self.delete_book()
             elif c == "5": break

    def member_menu(self):
         while True:
             print("---------------Member Menu---------------")
             print("1.Add 2.View 3.Search 4.Delete 5.Back")
             c = input("Choice : ")
             if c == "1": self.add_member()
             elif c == "2": self.view_members()
             elif c == "3": self.search_member()
             elif c == "4": self.delete_member()
             elif c == "5": break

    def report_menu(self):
          print("---------------Report Menu---------------")
          print("1.Issued 2.Available 3.Overdue")
          c = input("Choice : ")
          if c == "1": self.issued_books()
          elif c == "2":self. available_books()
          elif c == "3": self.overdue_books()

# ---------- START ----------
if __name__ == "__main__":
    lib = Library()
    lib.main_menu()