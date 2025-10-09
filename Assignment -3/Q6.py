# 6. Write a program to calculate profit or loss.

cost_price = float(input("enter cost price : "))
selling_price = float(input("enter selling price : "))

if cost_price > selling_price:
    loss = cost_price-selling_price
    print("loss of ", loss)
    
elif selling_price > cost_price :
    profit = selling_price - cost_price 
    print("Profit of ", profit)
else:
    print("No profit , No loss")