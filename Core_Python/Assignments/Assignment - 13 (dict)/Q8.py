# 8. Python Program to Count the Frequency of Words Appearing in a String Using
# a Dictionary


# 8. Python Program to Count the Frequency of Words Appearing in a String Using
# a Dictionary


def countFreq(d):
    freq = {}
    for value in d.values():
        if value in freq:
            freq[value] += 1
        else:
            freq[value] = 1
    return freq

d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 1}
ans = countFreq(d)
print(ans)
