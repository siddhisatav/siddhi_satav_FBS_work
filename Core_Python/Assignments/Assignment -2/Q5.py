# 3. Convert distant given in feet and inches into meter and centimeter.

F =int(input("enter feets"))
n =int(input("enter inches"))
total_cm = (F * 30.48) + (n * 2.54)
centimeters = total_cm % 100
meters = total_cm//100

print(f"{F} feet {n} inche = {meters} meter {centimeters} centimeter")








