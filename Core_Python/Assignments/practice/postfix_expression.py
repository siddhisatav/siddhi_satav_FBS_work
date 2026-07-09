def post_fix(arr):

     op = ['+','*','-','/']
     
     stack =[]
     for i in arr :
         if i in op :
             first=int(stack.pop())
             sec =int(stack.pop())
             
             if i == '+':
                 ans = first+sec
                 
             elif i == '-':
                  ans = first - sec
                  
                 
                 
             elif i == '*':
                  ans = first * sec
                 
                 
                 
             elif i == '/':
                 ans = first / sec
                
                 
                 
             stack.append(ans)
                 
                
                 
         else :
             stack.append(i)
             
             
     return stack[-1]
 
arr=['2','1','+','3','*']
res=post_fix(arr)
print(res)             
             
         

  