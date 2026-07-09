strr="Hello World"
#  answer 1
# print(strr[::-1])

# answer 2
words =strr.split(" ")
# print(words)


for i in range(len(words)):
    word =list(words[i])
    # print(len(words[i]))
    s=0
    e= len(word)-1
    temp=0
    while s<e:
         temp = word[s]
         word[s] = word[e]
         word[e] = temp
         s+=1
         e-=1
         
    words[i] = "".join(word)  # convert back to string

# print(words)
rev_str = " ".join(words)

sw=rev_str.split(" ")


w=list(sw)
st=0
et= len(w)-1
while st<et :
            temp = w[st]
            w[st]=w[et]
            w[et]=temp
            st+=1
            et-=1
        
sw = " ".join(w) 
print(sw)
    
    