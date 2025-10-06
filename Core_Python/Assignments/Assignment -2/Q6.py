cost = int(input("enter cost price :"))
discount = int(input("enter discount percent :"))
discount_amount = (discount/100) * cost
selling_price = cost - discount_amount
print("selling price is : ", selling_price)