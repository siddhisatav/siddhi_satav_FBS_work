# 7. WAP to print all integers upto n that aren’t divisible by 2 and 3.

n =int(input("enter the value of n : "))
print("Numbers aren’t divisible by 2 and 3. ")
for i in range(1,n+1):
    if(i %2 != 0 ) and (i%3 != 0 ):
        print(i)
        
    