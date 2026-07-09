li = [40,50,60,70,80,90]
print(li)
li.append(70)
print(li)

li2 = li.copy()
li3 = li 
li.clear()
print(li2)
print(li3)
print(id(li))
print(id(li2))
print(id(li3))

print(li2.count(60))
li2.insert(3,40)
print(li2)
print(li2.count(40))
li2.pop()
print(li2)
li2.remove(50)
print(li2)
li2.reverse()
print(li2)
