# 6. WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.

basic = int(input("enter basic salary : "))
da = (10/100)  * basic
ta = (12/100) * basic
hra = (15/100) * basic
print("DA :" , da)
print("TA :" , ta)
print("HRA :" , hra)

tatal_salary = da+ta+hra+basic

print("Tptal Salary : ",tatal_salary)