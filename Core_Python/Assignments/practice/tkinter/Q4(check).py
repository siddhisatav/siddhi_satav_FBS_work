from tkinter import *
from tkinter import messagebox
def check():
    val1=a.get()
    val2=b.get()
    val3=c.get()
    data = ''
    
    if val1 == 1 :
        data = data + "python\n"
        
    if val2 == 1:
        data = data + "java\n" 
        
    if val3 == 1 :
        data = data +"html\n"
        
    if data :
    #    messagebox.INFO(Message="submitted !!!!")
       print("course:" , data)
       output.config(text="data submitted. ")
    else :
        output.config(text="")
        messagebox.showerror("Error", message = "please select option!!! ")
if(__name__=="__main__"):
    w =Tk()
    w.geometry("200x400")
    
    a=IntVar()
    b=IntVar()
    c=IntVar()
    
    
    txt=Label(w,text="select options=")
    chk1 = Checkbutton(w,text = "python",variable=a) # no need to give value because it give 1 if selected and 0 if not select automatically 
    chk2=Checkbutton(w,text="java",variable = b)
    chk3 =Checkbutton(w,text="html",variable=c)
    bt=Button(w,text="submit",command=check)
    
    output = Label(w,text="")
    
    
    txt.pack()
    chk1.pack()
    chk2.pack()
    chk3.pack()
    bt.pack()
    output.pack()
    
    mainloop()