# 2. Implement a generator function that yields palindrome numbers.
# Palindromes are numbers that read the same backward as forward
# (e.g., 121, 1331). Generate palindromes lazily and infinitely.


def palindrom(num):
   
    temp = num 
    rev =0 
    while num > 0 :
        rev =rev * 10 + num % 10
        num //= 10
        
    if temp ==  rev :
        yield temp 
        
        
num =int(input("enter number : "))
res= palindrom(num)
res_list = list(res)

if res_list:
    
     print(f"palindrom numbers : {res_list[0]}")
        
    
else:
    print("not a plindrom number ")