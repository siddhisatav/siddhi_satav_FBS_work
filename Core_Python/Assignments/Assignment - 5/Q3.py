# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
total_cost = 0
no_of_passenger = int(input("Enter number of passenger :"))
per_ticket_cost = int(input("Enter per ticket cost : "))
for i in range (no_of_passenger):
  age = int(input(f"Enter age passenger {i+1} : "))
  
  if age < 12:
      discount_amount=30/100
      discount = per_ticket_cost - (per_ticket_cost*discount_amount)
      print("Price of ticket :", discount)
      
  elif age > 59 :
        discount_amount=50/100
        discount = per_ticket_cost - (per_ticket_cost*discount_amount)
        print("Price of ticket :", discount)
      
  else:
      discount = per_ticket_cost
      print("Price of ticket is : ",per_ticket_cost)
      
  total_cost +=discount
print("Total cost :", total_cost)