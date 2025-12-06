# 5. Write a Python program to find the longest common prefix of all
# strings. Use the Python set.

words = ["flower", "flow", "flight"]

# Start with the first word as prefix
prefix = words[0]

for word in words[1:]:
    while prefix and prefix not in word[:len(prefix)]:
        prefix = prefix[:-1]  # shorten prefix until it matches

print("Longest common prefix:", prefix)
