---

### 🔍 The Code:

```python
s = {12, 41, "jhansi", ["fedora", 25, 12.25, "burpsuite"], 152}
```

---

### ✅ Expected Behavior?

You're trying to create a set `s` that includes:

* Integers: `12`, `41`, `152`
* A string: `"jhansi"`
* A **list**: `["fedora", 25, 12.25, "burpsuite"]`

---

### ❌ What Actually Happens?

Running this code will throw a **`TypeError`**:

```python
TypeError: unhashable type: 'list'
```

---

### ❓ Why This Error Occurs

#### 📌 Rule for Sets in Python:

> **Every element in a set must be *hashable* (i.e., immutable)**.

* `int`, `str`, `float`, `tuple` ✅ → These are **hashable**
* `list`, `dict`, `set` ❌ → These are **unhashable**

---

### 🔬 What is "hashable"?

An object is **hashable** if:

1. It has a `__hash__()` method.
2. Its value doesn’t change over time (immutable).

Lists are **mutable**: you can change their content (e.g. `my_list[0] = 100`), which means their hash value could change. That breaks the contract required by sets (which rely on hashing for fast lookup and uniqueness).

---

### 🤔 Why Sets Require Hashable Items

* Sets use a **hash table** internally for fast operations like `in`, `add()`, and `remove()`.
* If an object can change, then its hash could change.
* If the hash changes, the set can't reliably track it — it's like losing the address of your object in memory.

---

### ✅ What You *Can* Do

If you want something like a list in a set, use **a tuple instead** (as long as the tuple contains only hashable elements):

```python
s = {12, 41, "jhansi", ("fedora", 25, 12.25, "burpsuite"), 152}
```

Now this works because `tuple` is immutable and hashable (assuming all its items are hashable).

---

### 🔁 Back to Your Question:

> **Can we change a value inside a list which is contained in a set?**

### ❌ No — because:

1. **You cannot even add a list to a set** — it will raise a `TypeError`.
2. Even if you somehow forced it in (e.g., using a wrapper object), **changing its content** would break the **hash consistency** needed by the set.

---

### ✅ Summary Table

| Type    | Mutable? | Hashable? | Can be in a set?                 |
| ------- | -------- | --------- | -------------------------------- |
| `int`   | No       | Yes       | ✅ Yes                            |
| `str`   | No       | Yes       | ✅ Yes                            |
| `tuple` | No       | Yes\*     | ✅ Yes (if contents are hashable) |
| `list`  | Yes      | No        | ❌ No                             |
| `dict`  | Yes      | No        | ❌ No                             |

---







---

## 🔐 What Does **Hashable** Mean in Python?

### ✅ Definition:

An object is **hashable** if it has a **fixed hash value for its lifetime**, which means:

* It can be used as a key in a **dictionary**
* It can be stored in a **set**

### ✅ Technically:

An object is **hashable** if:

1. It implements the `__hash__()` method.
2. It is **immutable** (its contents don’t change).

---

### 🔍 Why Does Python Use Hashing?

Hashing allows fast access and lookup in collections like:

* `dict` (keys must be hashable)
* `set` (elements must be hashable)

Example:

```python
print(hash(10))         # ✅ Works (int is hashable)
print(hash("hello"))    # ✅ Works (string is hashable)

my_list = [1, 2, 3]
print(hash(my_list))    # ❌ ERROR: list is unhashable
```

### ❌ Why `list`, `dict`, `set` are not hashable?

Because they are **mutable** — their contents can change:

```python
my_list = [1, 2, 3]
my_list[0] = 99  # changes the list
```

If something changes, its hash would change — and that **breaks sets and dicts** (which rely on consistent hashes).

---

## 🧊 What is `frozenset` in Python?

### ✅ Definition:

A `frozenset` is the **immutable version of a set**.

* You can create it like a set.
* You **cannot change it** (no `add()`, `remove()` allowed).
* But you **can use it** as a key in a dictionary or an element in a set (because it is **hashable**).

---

### 🔍 Example:

```python
fs = frozenset([1, 2, 3])
print(fs)  # frozenset({1, 2, 3})

# ✅ Can be added to a set
s = {fs, frozenset([4, 5])}
print(s)  # {frozenset({1, 2, 3}), frozenset({4, 5})}

# ❌ Cannot modify
fs.add(4)  # AttributeError: 'frozenset' object has no attribute 'add'
```

---

## 🔁 Comparison Table:

| Feature                        | `set` | `frozenset` |
| ------------------------------ | ----- | ----------- |
| Mutable                        | ✅ Yes | ❌ No        |
| Hashable                       | ❌ No  | ✅ Yes       |
| Can be in a set/dict key       | ❌ No  | ✅ Yes       |
| Supports set ops (union, etc.) | ✅ Yes | ✅ Yes       |

---

## 🧠 Summary

* **Hashable** = Immutable + Has a fixed `__hash__()` value.
* **Mutable types** like `list`, `dict`, `set` are **not hashable**.
* **frozenset** is like a `set` but immutable and **hashable**, so it can be used in places like:

  * Set of sets
  * Dict keys with set-like values

---

---

## ❌ **No, `frozenset` does not support indexing**.

---

### 📌 Why?

Because a `frozenset` (just like a regular `set`) is:

* **Unordered** → it doesn't maintain insertion order
* **Doesn’t support indexing or slicing**, like lists or tuples

So, trying to access it like this:

```python
fs = frozenset([10, 20, 30])
print(fs[0])  # ❌ Error!
```

will raise:

```
TypeError: 'frozenset' object is not subscriptable
```

---

## ✅ How to work around it

If you **really** need to access elements by index, you can convert the `frozenset` to a list or tuple first:

```python
fs = frozenset([10, 20, 30])
fs_list = list(fs)

print(fs_list[0])  # ✅ Will work, but order is not guaranteed
```

⚠️ **Important Note**: Since `frozenset` is unordered, the order in `fs_list` is not guaranteed to be the same every time.

---

---

### 🔁 **Python Data Types Comparison Table**

| Feature / Type            | `frozenset`                   | `set`                       | `tuple`                 | `list`                     | `dict`                          |
| ------------------------- | ----------------------------- | --------------------------- | ----------------------- | -------------------------- | ------------------------------- |
| **Mutable**               | ❌ No                          | ✅ Yes                       | ❌ No                    | ✅ Yes                      | ✅ Yes                           |
| **Hashable**              | ✅ Yes                         | ❌ No                        | ✅ Yes\*                 | ❌ No                       | ❌ No                            |
| **Allows Duplicates**     | ❌ No                          | ❌ No                        | ✅ Yes                   | ✅ Yes                      | ❌ No (unique keys only)         |
| **Ordered (Python 3.7+)** | ❌ No                          | ❌ No                        | ✅ Yes                   | ✅ Yes                      | ✅ Yes                           |
| **Indexing Support**      | ❌ No                          | ❌ No                        | ✅ Yes                   | ✅ Yes                      | ❌ No (but keys can act like it) |
| **Can be key in dict**    | ✅ Yes                         | ❌ No                        | ✅ Yes (if hashable)     | ❌ No                       | —                               |
| **Can be element in set** | ✅ Yes                         | ❌ No                        | ✅ Yes (if hashable)     | ❌ No                       | ❌ No                            |
| **Comprehension Support** | ✅ Yes                         | ✅ Yes                       | ❌ No                    | ✅ Yes                      | ✅ Yes                           |
| **Supports Iteration**    | ✅ Yes                         | ✅ Yes                       | ✅ Yes                   | ✅ Yes                      | ✅ Yes                           |
| **Typical Use Case**      | Unique, immutable collections | Unique, mutable collections | Fixed-size ordered data | Ordered, mutable sequences | Key-value mappings              |

---

### 🧠 Footnote:

* \* `tuple` is only hashable **if all of its elements are hashable**. For example:

  ```python
  hash((1, 2, 3))       # ✅ Works
  hash((1, [2, 3]))     # ❌ Fails (because list is unhashable)
  ```

---

### ✅ Summary Insights:

* Use `**list**` when you need **ordered, mutable** sequences.
* Use `**tuple**` when you need **ordered, immutable** sequences.
* Use `**set**` for **unique, unordered, mutable** values.
* Use `**frozenset**` for **unique, unordered, immutable** values.
* Use `**dict**` for **key-value** pair mappings with **unique keys**.

---

