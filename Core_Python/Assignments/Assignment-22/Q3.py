import re
from collections import Counter

def word_count(text):
    # Convert text to lowercase for case-insensitive counting
    text = text.lower()
    
    # Use regex to split text into words (ignoring punctuation)
    words = re.findall(r'\b\w+\b', text)
    
    # Count the frequency of each word
    frequency = Counter(words)
    
    return frequency

# Example usage
text = """
This is a simple example. This example shows how to count words!
Counting words, ignoring punctuation and case.
"""

result = word_count(text)
print("Word Frequencies:")
for word, count in result.items():
    print(f"{word}: {count}")
