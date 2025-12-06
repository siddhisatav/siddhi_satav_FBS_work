# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1
# # and n) in the Form (x,x*x).

def Num(n):
  
    dict = {}
    for i in range(1,n+1):  
      
      dict[i] = i*i
      
    return dict

n = int(input("enter value of n : "))
ans = Num(n)
print(ans)