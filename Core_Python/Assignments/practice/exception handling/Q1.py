try :
    li =[10,20,30,40]
    inn =int(input("enter index :"))
    print("value :" , li[inn])
    
except ValueError as e :
    print("error : " , e)
    
except AttributeError as e :
    print("error : " , e)
    
except IndexError as e:
    print("error : ",e )
    
except :
    print("something wents wrong !!")
    
else :
    print("sucessfully accessed !!")