# WAP to print pattern 

for i in range (0,7):
    for j in range (0,7):
        if i == 0 or i == 6:
            
            print("*" , end = " ")
        # elif (i==1 and j == 5) or (i == 2 and j ==4 ) or (i == 3 and j== 3) or (i==4 and j==2) or (i == 5 and j == 1 ):
        elif i + j == 6:
            print("*" , end = " ")
        else :
            print(" " , end = " ")
            
    print()
    
    