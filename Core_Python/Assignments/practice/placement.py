# def fun(num):
    
#     power = len(str(num))
#     sum = 0
#     temp = num 
#     while num > 0 :
#         digit = num % 10
#         sum += digit**power  
#         num //=10
    
    
#     if sum == temp :
#         print(temp,"armstrong")
    
    
#     else :
#         print("not armstrong")
        
        
# num = int(input("enter num : "))
# fun(num)



# def factt(num):
#     f = 1
#     for i in range (1,num+1):
#         f *= i 
#     return f 

# def demo(num):
#     temp = num
#     summ = 0 
#     while num > 0 :
#         digit = num % 10 
#         summ += factt(digit)
#         num //=10
        
#     if temp == summ:
#         print(temp , "strong number")

#     else:
#         print("not strong number ")
        
# num = int(input("enter number : "))
# demo(num)    


# def demo (num):
#     summ=0
#     temp = num 
#     for i in range (1 , num):
#         if num % i == 0 :
#             summ += i 
      
            
#     if temp == summ :
#         print("perfectNumber")
        
#     else:
#         print("not perfect number ")
 
# num = int(input("enter num : "))               
# demo(num)


# def demo (num):
#     temp = num 
#     rev = 0
#     while(num > 0 ):
#         digit = num %10 
#         rev = rev * 10 + digit
#         num //=10
        
#     if rev == temp :
#         print("number is palindrom ")
        
#     else :
#         print("number is not palindrom")
        
# num = int(input("enter number :"))
# demo(num)

def demo(s):
    # rev = s[::-1]
    temp = s
    ch = ""
    for i in s :
        ch = i +ch 
        
    if ch == temp :
        print("palindrom")
        
    else:
        print("not palindrom")
        
         
s = input("enter string : ")
demo(s)   
        
    
    
