# 5. Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.

def checkElement(li,element):
    count = 0 
    for i in range (len (li)):
        if li[i] == element:
             count +=1
    return count
            
    
li =[ 23,33,45,56,89,45,99]
element =int(input("enter the element : "))
result = checkElement(li,element)
if result > 0 :
    print(f"{element} is present in list")
    print("count of element present in list :  ",result ) 
    
else:
    print(element,"Element not present ")
    
       