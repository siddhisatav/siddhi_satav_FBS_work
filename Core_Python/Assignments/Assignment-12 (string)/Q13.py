# 13. Python Program to count number of digits and letters in a string.

def countDigitLetter(str):
    count_digit = 0
    count_letter = 0
    for i in str:
        if i >= '0' and i <= '9' :
            count_digit +=1
            
        elif ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
            count_letter += 1
            
    return count_letter,count_digit

str = input("enter string : ")
ans = countDigitLetter(str)
print("count of digit is : ", ans[1])
print("count of letter is : ",ans[0])
            