from tkinter import * 
from tkinter import messagebox # sunmodule
def add():
    a = int(e1.get())
    b=int(e2.get())
    c= a+b
    # terminal var ans print hota
    print(f"add is : ", c ) 
    # screen war ans print hota
    # result.config(text=c)
    messagebox.showinfo("output" , message= c) 
    

w =Tk()
w.title("Addition")
w.geometry("500x650")

l1 = Label(w,text="enter no1 = " )
l1.grid(row = 0 , column = 0 )
e1 = Entry()
e1.grid(row=0,column=1)

l2=Label(w,text="enter no2 = ")
l2.grid(row = 1,column=0)
e2 =Entry()
e2.grid(row=1,column=1)

result = Label(w,text="")
result.grid(row = 3 , column = 1)
Button(w,text="submit" , command=add).grid(row=2,column=1)
w.mainloop()