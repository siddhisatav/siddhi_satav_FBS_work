l =int(input("enter l"))
b=int(input("enter b"))
interiror_cost = int(input("enter interiror cost"))
exteriror_cost = int(input("enter exteriror cost"))

area = l*b
wall1_in = interiror_cost * area
wall1_exteriror = exteriror_cost * area


total_cost = wall1_in + wall1_exteriror

# interiror_walls = wall1_in * 8 
# exteriror_walls =wall1  * 6 

print("area : ", area)
print("interior cost :" , interiror_cost )
print("exteriror cost :" , exteriror_cost  )
print("total_cost" , total_cost)


