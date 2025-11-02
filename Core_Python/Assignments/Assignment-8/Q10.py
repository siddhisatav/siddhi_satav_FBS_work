# 10. Write a program to check if entered year is a leap year or not.

def check_leap_year ():
    year = int(input("enter year : "))
    if (year %400 == 0) or (year % 4 ==0 and year % 100 !=0):
        print(year , "is a Leap year.")
    else:
        print(year , "is not leap year.")
check_leap_year()