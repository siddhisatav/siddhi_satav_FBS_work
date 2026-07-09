from threading import Thread , Lock 

def withdraw(amt):
    lock.acquire()
    with open("C:/Users/Admin/OneDrive/Desktop/FBS/Core_Python/practice/tkinter/balance.txt","r") as fp:
        bal = int(fp.read())
    bal = bal - amt
    
    with open("C:/Users/Admin/OneDrive/Desktop/FBS/Core_Python/practice/tkinter/balance.txt","w") as fp:
        fp.write(str(bal))
    lock.release()
    
    
def deposite(amt):
    lock.acquire()
    
    with open("C:/Users/Admin/OneDrive/Desktop/FBS/Core_Python/practice/tkinter/balance.txt","r") as fp:
        bal = int(fp.read())
   
    bal = bal + amt
    
    with open("C:/Users/Admin/OneDrive/Desktop/FBS/Core_Python/practice/tkinter/balance.txt","w") as fp:
        fp.write(str(bal))
    lock.release()
    
    
if (__name__ == "__main__") :
    global lock
    lock = Lock()
    t1 = Thread(name ="T1" , target= withdraw , args=(2, ))
    t2 = Thread(name = "T2" , target = deposite , args=(10, ))
    
    t2.start()
    t1.start()
    