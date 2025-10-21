# 6. Write a program to print prime numbers between 1 to 100.
print("Prime numbers between 1 and 100:")

for num in range(2, 101):  # Start from 2
    is_prime = True
    for i in range(2, num):  # Check from 2 up to num-1
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end="\t")