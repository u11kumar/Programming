# Python Notes 📝

## Table of Contents 📑
1. [Strings 📜](#strings-)
2. [List 📋](#list-)
3. [Dictionary 📖](#dictionary-)
4. [Tuples 🧱](#tuples-)
5. [Sets 🧩](#sets-)

---

## Strings 📜

### Basic Operations
```python
s = "Hello Python!"
```

| Operation | Example | Result |
|-----------|---------|--------|
| Length | `len(s)` | `13` |
| Indexing | `s[0]` | `'H'` |
| Slicing | `s[6:12]` | `'Python'` |
| Concatenation | `s + " 🚀"` | `'Hello Python! 🚀'` |
| Repetition | `s * 2` | `'Hello Python!Hello Python!'` |

### Advanced Operations 🔥
```python
# String methods
"python".capitalize()   # 'Python'
"PYTHON".casefold()     # 'python'
"python".center(10, '*') # '**python**'
"python".find('th')     # 2
"python".isalnum()      # True
"3.14".isnumeric()      # False
" ".join(["Python", "Rocks"]) # 'Python Rocks'
```

---

## List 📋

### Basic Operations
```python
my_list = [1, 2, 3, 'Python', True]
```

| Operation | Example | Result |
|-----------|---------|--------|
| Append | `my_list.append(4)` | `[1, 2, 3, 'Python', True, 4]` |
| Extend | `my_list.extend([5,6])` | `[1, 2, 3, 'Python', True, 4, 5, 6]` |
| Insert | `my_list.insert(0,0)` | `[0, 1, 2, 3, 'Python', True, 4, 5, 6]` |
| Remove | `my_list.remove('Python')` | `[0, 1, 2, 3, True, 4, 5, 6]` |
| Pop | `my_list.pop()` | `6` (returns removed element) |

### Advanced Operations 🔥
```python
# List comprehension
squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Sorting
sorted([3,1,2], reverse=True)  # [3, 2, 1]

# Filter
list(filter(lambda x: x%2==0, [1,2,3,4]))  # [2, 4]

# Map
list(map(str, [1,2,3]))  # ['1', '2', '3']
```

---

## Dictionary 📖

### Basic Operations
```python
my_dict = {'name': 'Alice', 'age': 25, 'job': 'Developer'}
```

| Operation | Example | Result |
|-----------|---------|--------|
| Access | `my_dict['name']` | `'Alice'` |
| Add/Update | `my_dict['salary'] = 50000` | Adds new key-value |
| Delete | `del my_dict['age']` | Removes key 'age' |
| Keys | `my_dict.keys()` | `dict_keys(['name', 'job', 'salary'])` |
| Values | `my_dict.values()` | `dict_values(['Alice', 'Developer', 50000])` |

### Advanced Operations 🔥
```python
# Dictionary comprehension
{x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Merging dictionaries (Python 3.9+)
dict1 = {'a': 1}
dict2 = {'b': 2}
dict1 | dict2  # {'a': 1, 'b': 2}

# Default values
from collections import defaultdict
dd = defaultdict(int)
dd['key'] += 1  # Automatically initializes to 0
```

---

## Tuples 🧱

### Basic Operations
```python
my_tuple = (1, 2, 3, 'Python')
```

| Operation | Example | Result |
|-----------|---------|--------|
| Access | `my_tuple[0]` | `1` |
| Slicing | `my_tuple[1:3]` | `(2, 3)` |
| Count | `my_tuple.count(2)` | `1` |
| Index | `my_tuple.index('Python')` | `3` |

### Advanced Operations 🔥
```python
# Tuple unpacking
a, b, *rest = (1, 2, 3, 4)  # a=1, b=2, rest=[3,4]

# Named tuples
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)  # p.x = 11, p.y = 22

# Zip to tuple
tuple(zip([1,2], ['a','b']))  # ((1, 'a'), (2, 'b'))
```

---

## Sets 🧩

### Basic Operations
```python
my_set = {1, 2, 3, 4}
other_set = {3, 4, 5, 6}
```

| Operation | Example | Result |
|-----------|---------|--------|
| Union | `my_set | other_set` | `{1, 2, 3, 4, 5, 6}` |
| Intersection | `my_set & other_set` | `{3, 4}` |
| Difference | `my_set - other_set` | `{1, 2}` |
| Symmetric Diff | `my_set ^ other_set` | `{1, 2, 5, 6}` |
| Add | `my_set.add(5)` | `{1, 2, 3, 4, 5}` |

### Advanced Operations 🔥
```python
# Set comprehension
{x for x in 'abracadabra' if x not in 'abc'}  # {'d', 'r'}

# Frozen sets (immutable)
frozen = frozenset([1,2,3])

# Remove duplicates from list
list(set([1,2,2,3]))  # [1, 2, 3]
```

---

# Advanced Python Concepts 🚀

## For All Collections
- **Iterators**: `iter()`, `next()`
- **Generators**: `yield` keyword
- **Comprehensions**: List/Dict/Set comprehensions
- **Memory Views**: `memoryview()` for memory efficiency
- **Deep vs Shallow Copy**: `copy()`, `deepcopy()`

# 🔥 Advanced Python Concepts [Deatiled] 🚀

These concepts apply to all core data types (like lists, dictionaries, tuples, etc.) and help you write **faster**, **cleaner**, and **more memory-efficient** code.

---

## ✅ Iterators: `iter()` and `next()`

### What is an Iterator?

An **iterator** is an object that enables you to traverse through a collection (like a list, tuple, etc.) **one item at a time**, using `next()`.

### How it works:

```python
numbers = [10, 20, 30]
it = iter(numbers)  # Get iterator

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
# print(next(it)) would raise StopIteration
```

> Use iterators when you want to control how you loop over data or work with large data sources lazily.

---

## ✅ Generators: `yield` Keyword

### What is a Generator?

A **generator** is a special type of iterator that yields values **on the fly** using `yield` instead of returning them all at once (like a list does).

### Example:

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = count_up_to(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
```

> Generators are **memory-efficient** for working with large or infinite sequences.

---

## ✅ Comprehensions: List / Dict / Set

### What is a Comprehension?

A **comprehension** is a concise way to create collections using a single line of code.

### 📋 List Comprehension

```python
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

### 📖 Dictionary Comprehension

```python
squared_dict = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, ..., 4: 16}
```

### 🧩 Set Comprehension

```python
evens = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}
```

> They are cleaner and often faster than loops.

---

## ✅ Memory Views: `memoryview()`

### What is `memoryview()`?

A `memoryview` lets you **access memory directly without copying** data. It’s very efficient for handling large binary data like files or images.

### Example:

```python
data = bytearray(b'hello')
mv = memoryview(data)
mv[0] = 72  # changes first byte to 'H'
print(data)  # bytearray(b'Hello')
```

> Use `memoryview()` to avoid making copies of large datasets when manipulating them.

---

## ✅ Deep vs Shallow Copy: `copy()` vs `deepcopy()`

### Shallow Copy (`copy.copy()`):

Copies **only the top-level object**, not the nested objects inside.

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
shallow[0][0] = 99
print(original)  # [[99, 2], [3, 4]] — changed!
```

### Deep Copy (`copy.deepcopy()`):

Copies **everything recursively**, including nested elements.

```python
deep = copy.deepcopy(original)
deep[0][0] = 100
print(original)  # [[99, 2], [3, 4]] — unaffected!
```

> Use `deepcopy()` when you need full isolation of copied data.

---

### Summary Table 📊

| Concept        | Key Function/Keyword | Purpose                                      |
| -------------- | -------------------- | -------------------------------------------- |
| Iterators      | `iter()`, `next()`   | Step-by-step iteration through data          |
| Generators     | `yield`              | Efficiently generate values one-by-one       |
| Comprehensions | `[x for x in y]`     | Short syntax for creating lists, sets, dicts |
| Memory Views   | `memoryview()`       | Efficient data manipulation without copying  |
| Shallow Copy   | `copy()`             | Copy only outer object                       |
| Deep Copy      | `deepcopy()`         | Recursively copy all nested objects          |

---
