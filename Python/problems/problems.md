
---
## 📜 Strings – Advanced Problems

### Problem 1: Most Frequent Word (ignoring case and punctuation)

> Given a paragraph, return the most frequent word (ignore case and punctuation).

```python
text = "Python is great. Yes, PYTHON is really great!!"
# Output: "python"
```

---

### Problem 2: Run-Length Encoding

> Compress the string using Run-Length Encoding. Consecutive characters should be counted.

```python
s = "aaabbccddd"
# Output: "a3b2c2d3"
```

---

### Problem 3: Palindrome Rearrangement

> Write a function to check if the characters of a string can be rearranged to form a palindrome.

```python
can_form_palindrome("civic") → True  
can_form_palindrome("ivicc") → True  
can_form_palindrome("hello") → False
```

---

## 📖 Dictionaries – Advanced Problems

### Problem 1: Group Words by Anagram

> Group a list of words into sets of anagrams using a dictionary.

```python
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

---

### Problem 2: Nested Dictionary Update

> Merge two nested dictionaries (values may also be dicts).

```python
dict1 = {'a': 1, 'b': {'x': 2}}
dict2 = {'b': {'y': 3}, 'c': 4}
# Output: {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
```

---

### Problem 3: Invert a Dictionary with List Values

> Given a dictionary where values are lists, invert it to get value-to-key mapping.

```python
d = {'a': [1, 2], 'b': [2, 3]}
# Output: {1: ['a'], 2: ['a', 'b'], 3: ['b']}
```

---

## 🧱 Tuples – Advanced Problems

### Problem 1: Tuple Sort by Second Element

> Sort a list of tuples based on the second item.

```python
data = [(1, 3), (4, 1), (2, 2)]
# Output: [(4, 1), (2, 2), (1, 3)]
```

---

### Problem 2: Detect Circular Tuple Shift

> Check if one tuple is a circular rotation of another.

```python
t1 = (1, 2, 3, 4)
t2 = (3, 4, 1, 2)
# Output: True
```

---

### Problem 3: Immutable Data Tracker

> Use `namedtuple` to track user data and compute average age.

```python
User = namedtuple('User', ['name', 'age'])
users = [User('Alice', 30), User('Bob', 40)]
# Output: average age = 35.0
```

---

## 🧩 Sets – Advanced Problems

### Problem 1: Common Elements in All Sets

> Given a list of sets, find elements common to all of them.

```python
sets = [{1, 2, 3}, {2, 3, 4}, {3, 2, 5}]
# Output: {2, 3}
```

---

### Problem 2: Symmetric Difference Across Multiple Sets

> Find items that are in an **odd number** of sets.

```python
sets = [{1, 2}, {2, 3}, {1, 3, 4}]
# Output: {4}
```

---

### Problem 3: Remove Anagrams Using Sets

> Given a list of words, remove all anagrams, keeping only one from each group.

```python
words = ['code', 'deco', 'node', 'done']
# Output: ['code', 'node'] (or similar unique set)
```

---

## 📋 Lists – Advanced Problems

### Problem 1: Flatten a Nested List (recursive)

> Write a function to flatten a list of arbitrarily nested lists.

```python
nested = [1, [2, [3, 4], 5], 6]
# Output: [1, 2, 3, 4, 5, 6]
```

---

### Problem 2: Sliding Window Maximum

> Return a list of max values in each sliding window of size `k`.

```python
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
# Output: [3, 3, 5, 5, 6, 7]
```

---

### Problem 3: Sublist Sum Closest to Zero

> Find the sublist (contiguous) whose sum is closest to 0.

```python
arr = [1, 2, -3, 4, -2]
# Output: Sublist [-3, 4, -2] → sum = -1 (closest to 0)
```

---

Would you like **solutions** to these, or should I turn them into a PDF worksheet or notebook format?
