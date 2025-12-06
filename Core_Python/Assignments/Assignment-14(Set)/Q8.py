# 8. Write a Python program to find all the anagrams and group them
# together from a given list of strings.

def anagramsGroup(li):
    dict = {}
    for i in li :
        key = ''.join(sorted(i))
        if key in dict :
            dict[key].append(i)
            
        else :
            dict[key] =[i]

    return dict

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = anagramsGroup(words)
print("Grouped Anagrams:", groups)
            
    