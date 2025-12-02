# 9. Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String


def demo(str):
    count_word = 0
    count_char = 0
    words = str.split()
    
    count_char = len(str)
    count_word = len(words)
    
    return count_word, count_char



str = input("enter string :")
ans = demo(str)
print("Number of words : ", ans[0])
print("Number of characters  : ", ans[1])
