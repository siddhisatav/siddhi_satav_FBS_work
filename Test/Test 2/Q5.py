p1=int(input("enter product 1 price : "))
p2=int(input("enter product 2 price : "))
p3=int(input("enter product 3 price : "))
p4=int(input("enter product 4 price : "))
p5 =int(input("enter product 5 price : "))

total_cost = p1+p2+p3+p4+p5

gst =18 
total_bill = total_cost + (total_cost *gst/100)

print("total bill is : " ,total_bill)