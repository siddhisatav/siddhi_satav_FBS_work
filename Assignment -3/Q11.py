# 11. Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
total =0
for i in range (1, 6):
    age = int(input(f"enter age {i}:"))
    ticket_price= int(input(f"enter ticket price {i} : "))
    
    if age <= 12 :
        discount = ticket_price * 0.3
        amount_to_pay = ticket_price - discount 
        
        
    elif age >=59:
        discount = ticket_price * 0.5
        amount_to_pay = ticket_price -discount
        
    else :
        amount_to_pay = ticket_price
        
        
    print (f"Amount to pay {i} :  {amount_to_pay}")
    
    total +=amount_to_pay
    
print("Total amount to pay : ", total)
    
    
        
    