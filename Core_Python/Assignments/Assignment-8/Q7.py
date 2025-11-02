# 7. Write a program to find sum of digits of a number.

def demo():
    sum_num=0
    n =int(input("enter a number : "))
    while n>0:
      digit = n % 10  #get last digit
      sum_num +=  digit   #sum of digits
      n=n//10     #remove last digit
    print("Sum of digits of number : ", sum_num)
    

demo()