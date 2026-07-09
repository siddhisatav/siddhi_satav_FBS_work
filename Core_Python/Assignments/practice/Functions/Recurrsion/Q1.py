def sos(n):
    if(n<= 0 ):
        return 0 
    else:
        return n + sos(n-1)
    
result = sos ( 5)
print(result)
    