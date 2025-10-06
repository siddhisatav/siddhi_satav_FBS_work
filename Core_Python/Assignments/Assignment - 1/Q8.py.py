# 8. Write a program to convert days into years, weeks and days.

days =int(input("enter days :"))

years = days // 365
dayss = days%365
weeks = dayss // 7
dayss=dayss%7

print(f"Years : {years} , Days : {dayss} , Weeks : {weeks}")