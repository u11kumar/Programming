'''
### Problem 1: Most Frequent Word (ignoring case and punctuation)

> Given a paragraph, return the most frequent word (ignore case and punctuation).

```python
text = "Python is great. Yes, PYTHON is really great!!"
# Output: "python"
```
'''

from collections import Counter
import string

def most_frequent_word(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation manually
    for char in string.punctuation:
        text = text.replace(char, " ")

    # Split into words
    words = text.split()

    # Count words
    counts = Counter(words)

    # Return the most frequent word
    return counts.most_common(1)[0][0]

text = "Hello world! Hello everyone. This world is beautiful."
print(most_frequent_word(text))  # Output: "hello"

