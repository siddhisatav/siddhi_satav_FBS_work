from tkinter import *
from tkinter import messagebox

def change():
    val=x.get()
    if val == 1:
        w.config(background="black")
        
    elif val == 2:
        w.config(background="pink")
    
    elif val == 3:
        w.config(background="blue")
        
    elif val == 4:
        w.config(background="white")
        
    else:
        messagebox.showerror("error",message="please select option !!!")
        
        
if (__name__ == '__main__' ):
    w = Tk()
    w.geometry("200x300")
    x = IntVar()
    
    txt = Label(w,text="please select the color :")
    
    r1=Radiobutton(w,text = "black", variable= x , value= 1)
    r2=Radiobutton(w,text = "pink" , variable=x,value=2)
    r3=Radiobutton(w,text="blue",variable = x ,value = 3)
    r4 = Radiobutton(w,text="white",variable=x,value =4)
    
    bt=Button(w,text="do it",command=change)
    
    txt.grid(row=1,column=1)
    
    r1.grid(row=2,column=1)
    r2.grid(row=3,column=1)
    r3.grid(row=4,column=1)
    r4.grid(row=5,column=1)
    bt.grid(row=6,column=1)
    
    w.mainloop()
    
    