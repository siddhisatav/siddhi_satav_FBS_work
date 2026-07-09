tu = (10)
print(type(tu))

tu =(10,20)
print(type(tu))

tu = ()
print(type(tu))

tu = (10,3.14,"a")
print(type(tu))
print(tu)
print(tu[0])


import sys
tu = ()
li=[]
print(sys.getsizeof(tu))
print(sys.getsizeof(li))

tu =(12,22,33)
li = [22,33,44]
print(sys.getsizeof(tu))
print(sys.getsizeof(li))
