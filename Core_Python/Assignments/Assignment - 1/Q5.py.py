# 6. Write a Program to input two angles from user and find third angle of the triangle


angle_1 = int(input("enter first angle"))
angle_2 = int(input("enter second angle"))

sum_of_two_angle = angle_1 + angle_2

Third_angle = 180-sum_of_two_angle 

print("Third angle : " ,Third_angle )

