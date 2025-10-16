year = int (input("enter year "))

if year % 4 ==0:
    if year % 100 ==0 :
        if year %400 == 0 :
            print(year, "year is leap year " )
            
        else:
            print(year,"year is not leap year ")
            
    else:
        print(year ,"year is leap year")
        
else:
    print(year ,"year is not leap year")