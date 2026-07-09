from tkinter import * 

w = Tk()
w.geometry("600x700")

w.title("hii")
# li = Label(w,text="hii1").grid(row = 0, column = 0 )
# li = Label(w,text="hii2").grid(row = 0, column = 1 )
# li = Label(w,text="hii3").grid(row = 1, column = 1 )


li = Label(w,text="hii1")
li.pack()

li = Label(w,text = "hiiiiiiiii").place(x = 100,y=200)

w.mainloop()
