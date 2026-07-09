from tkinter import *
from tkinter import messagebox



def clearscreen():
    for widget in w.winfo_children():
        widget.destroy()

def empManage():
    def clearData():
        id_entry.delete(0,END)
        name_entry.delete(0,END)
        sal_entry.delete(0,END)
        id_entry.focus() #after deleting cursor should focus again on id
        
        
    def loaddata():
          with open("C:/Users/Admin/OneDrive/Desktop/FBS/Core_Python/practice/tkinter/emp.txt","r")as fp :
            for line in fp :
                mylist.insert(END,line)
        
    def addEmp():
        id = id_entry.get()
        nn = name_entry.get()
        sal = sal_entry.get()
        emp_data = f"{id}, {nn}, {sal}"
        with open("C:/Users/Admin/OneDrive/Desktop/FBS/Core_Python/practice/tkinter/emp.txt","a")as fp :
            fp.write(emp_data+'\n')
        mylist.insert(END,emp_data)
        
        clearData()
        
    def delEmp():
         with open("C:/Users/Admin/OneDrive/Desktop/FBS/Core_Python/practice/tkinter/emp.txt","r")as fp :
             allemps = []
             for line in fp :
                 emp_data = line.split(', ')
                 if(id != emp_data[0]):
                     allemps.append(line)
                     
         with open("C:/Users/Admin/OneDrive/Desktop/FBS/Core_Python/practice/tkinter/emp.txt","w")as fp :
             for line in allemps :
                 fp.write(line)
                 
         mylist.delete(0,END)
                
         loaddata()
             
         
    
    def selEmp():
        clearData()
        data = mylist.get(ACTIVE)
        emp_data = data.split(",")
        print(emp_data)
        id_entry.insert(0,emp_data[0])
        name_entry.insert(0,emp_data[1])
        sal_entry.insert(0,emp_data[2])
        
        
    
    def updEmp():
         emp_id = id_entry.get()
         nn = name_entry.get()
         sal = sal_entry.get()
         
         if emp_id == "":
            messagebox.showerror("Error", "Select employee to update")
            return

         updated = False
         allemps = []

         
         with open("C:/Users/Admin/OneDrive/Desktop/FBS/Core_Python/practice/tkinter/emp.txt","r")as fp :
             allemps = []
             for line in fp :
                 emp_data = line.split(', ')
                 if(emp_id == emp_data[0]):
                     allemps.append(f'{emp_id},{nn},{sal}\n')
                     updated = True
                 else:
                     allemps.append(line)
              
         if updated:       
             with open("C:/Users/Admin/OneDrive/Desktop/FBS/Core_Python/practice/tkinter/emp.txt","w")as fp :
                 for line in allemps :
                     fp.write(line)
                 
             mylist.delete(0,END)
                
             loaddata()
             clearData()
             messagebox.showinfo("Success", "Employee updated successfully")
         
         else:
             messagebox.showerror("Error", "Employee ID not found")
         
        
    
    
    clearscreen()
    
    frame1=Frame(w)
    frame2 = Frame(w)
    frame3=Frame(w)
    
    id_txt = Label(frame1 , text="ID : ",pady = 5)
    id_entry = Entry(frame1)
    name_txt=Label(frame1,text = "NAME : ",pady = 5)
    name_entry  =Entry(frame1)
    sal_txt = Label(frame1,text = "SALARY : ",pady = 5)
    sal_entry = Entry(frame1)
    
    id_txt.grid(row=1,column =1)
    id_entry.grid(row = 1,column =2)
    name_txt.grid(row = 2, column =1)
    name_entry.grid(row = 2,column= 2)
    sal_txt.grid(row = 3,column = 1 )
    sal_entry.grid(row = 3,column = 2)
    frame1.pack(pady=5)
    
    add_btn=Button (frame2,text="ADD",command = addEmp)
    del_btn = Button(frame2 ,text = "DELETE",command =delEmp )
    sel_btn = Button(frame2 , text = "SELECT" , command=selEmp)
    upd_btn=Button(frame2 , text = "UPDATE" , command= updEmp)
    
    add_btn.pack(side =LEFT)
    del_btn.pack(side=LEFT)
    sel_btn.pack(side=LEFT)
    upd_btn.pack(side=LEFT)
    frame2.pack(pady=5)
    
    
    scrollbar = Scrollbar(frame3)
    scrollbar.pack(side = RIGHT , fill=Y)
    mylist = Listbox(frame3 , yscrollcommand=scrollbar.set,height =20 , width=40)
    mylist.pack(side=LEFT , fill = BOTH)
    scrollbar.config(command=mylist.yview)
    frame3.pack(pady=5)
    
    loaddata()
    
    
    
    
def login():
    uid =user_entry.get()
    passwr = pass_entry.get()
    if(uid == "admin" and passwr == "1234"):
        empManage()
    else:
        messagebox.showerror("error",message= " invaild pass")
    
    
def main():
   
    global user_entry
    global pass_entry
    user = Label(w,text="username")
    user_entry = Entry(w)
    password = Label(w,text = "password")
    pass_entry = Entry(w)
    btn = Button(w,text="login",command=login)
    
    user.pack()
    user_entry.pack()
    password.pack()
    pass_entry.pack()
    btn.pack()
    
if (__name__ == "__main__"):
    w = Tk()
    w.title("EMS")
    w.geometry("200x400")
    
    
    
    # main()
    
    empManage()
    w.mainloop()
    