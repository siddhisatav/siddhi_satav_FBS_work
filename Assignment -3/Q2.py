# 2. Write a program to input any alphabet and check whether it is vowel or consonant.
v = ["a","e","i","o","u","A","E","I","O","U"]

character = input("enter alphabet : ")
if character in v :
    print("character is Vowel")
    
else : 
    print("character is Consonant")