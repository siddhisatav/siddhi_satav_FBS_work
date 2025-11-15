# 9. Write a program to calculate the m to the power n using recursion.

def power(m ,n ):
    if n ==0 :
        return 1
    return m *power(m,n-1)


m = float(input("Enter base (m): "))
n = int(input("Enter exponent (n): "))
print(f"{m} to the power {n} is {power(m, n)}")