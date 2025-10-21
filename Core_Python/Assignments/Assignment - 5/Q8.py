# 8. Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms


# a. 1! + 2! + 3! + 4! + .....n!
n = int(input("enter n value "))

sum_fact =0 
fact = 1
for i in range (1,n+1):
    fact*=i
sum_fact += fact 
    
print("factorial is : " , sum_fact)



# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
print("----exponent----")
A = int(input("enter value of n :"))
sum_exp=0
for j in range (1,A+1):
    expo = A**j
    sum_exp +=expo
    
print("Exponential : " , sum_exp)


# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
print("---------------")
b = int(input("Enter b: "))
sum_series = 2**b - 1
print("Sum =", sum_series)

# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
print("-------------")
a= int(input("Enter value of a :"))
s=0
for i in range (1,11):
  s+=a**i/i

print("Sum of the series S ",s)

# e. x - x2/3 + x3/5 - x4/7 + .... to n terms
print("---------------")
x = float(input("Enter value of x: "))
n = int(input("Enter number of terms: "))
S = 0

for i in range(1, n + 1):
    term = ((-1)**(i - 1)) * (x**i) / (2*i - 1)
    S += term
    
print("sum of the series = " , S)