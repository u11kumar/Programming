
---

### ✅ Code:

```python
s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))
```

---

### 💡 Step-by-Step Explanation:

#### 1️⃣ `s = set()`

* Creates an empty set.
* Set is a **collection of unique, unordered elements**.

  👉 `s = {}`

---

#### 2️⃣ `s.add(20)`

* Adds the integer `20` to the set.

  👉 `s = {20}`

---

#### 3️⃣ `s.add(20.0)`

* Adds the **float** `20.0` to the set.
* BUT: In Python, **`20` and `20.0` are considered equal**, because:

  ```python
  20 == 20.0      # True
  hash(20) == hash(20.0)  # Also True
  ```

✅ So `20.0` **does not get added** to the set — it is **seen as a duplicate** of `20`.

👉 `s = {20}`  (still just one element)

---

#### 4️⃣ `s.add('20')`

* Adds the **string `'20'`** to the set.
* Strings are not equal to numbers:

  ```python
  '20' == 20     # False
  '20' == 20.0   # False
  ```

✅ So `'20'` is **added as a new, unique element**.

👉 `s = {20, '20'}`

---

#### 5️⃣ `print(len(s))`

* The set has two elements: `20` (int) and `'20'` (str)

✅ **Output:**

```python
2
```

---

### 🔍 Final Set Contents:

```python
{20, '20'}
```

---

### ✅ Summary:

| Element Added  | Is It Unique? | Reason                            |
| -------------- | ------------- | --------------------------------- |
| `20` (int)     | ✅ Yes         | First element                     |
| `20.0` (float) | ❌ No          | Equal to `20` (same value & hash) |
| `'20'` (str)   | ✅ Yes         | A different type (`str` vs `int`) |

---

### 🧠 Key Concept:

> In Python, sets determine uniqueness using **`==`** and **`hash()`**.
> If `a == b` and `hash(a) == hash(b)`, they are **treated as the same** in a set.

