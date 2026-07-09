strr="hello netsetos"

# word = str.split(" ")
# size=len(word)
# print(word)
# len_word = len(word[size-1])
# print(len_word)

len_str=0
count=0
for _ in strr:
      len_str +=1
      
i = len_str-1
# print(i)
# while(i>=0 and i ==" "):
#     i-=1
    
while(i>=0 and strr[i] != " "):
    count+=1
    i-=1
    
    
print("count =", count)
      
