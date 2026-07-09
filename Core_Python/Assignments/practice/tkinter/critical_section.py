from threading import Thread 

def withdraw(amt):
    with open("C:/Users/Admin/OneDrive/Desktop/FBS/Core_Python/practice/tkinter/balance.txt","r") as fp:
        bal = int(fp.read())
    bal = bal - amt
    
    with open("C:/Users/Admin/OneDrive/Desktop/FBS/Core_Python/practice/tkinter/balance.txt","w") as fp:
        fp.write(str(bal))
        
def deposite(amt):
    with("C:/Users/Admin/OneDrive/Desktop/FBS/Core_Python/practice/tkinter/balance.txt","r") as fp:
        bal = int(fp.read())
   
    bal = bal + amt
    
    with("C:/Users/Admin/OneDrive/Desktop/FBS/Core_Python/practice/tkinter/balance.txt","w") as fp:
        fp.write(str(bal))
    
if (__name__ == "__main__") :
    t1 = Thread(name ="T1" , target= withdraw , args=(2000, ))
    t2 = Thread(name = "T2" , target = deposite , args=(10000, ))
    
    t2.start()
    t1.start()
    