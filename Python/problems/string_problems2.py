'''

### Problem 2: Run-Length Encoding

> Compress the string using Run-Length Encoding. Consecutive characters should be counted.

```python
s = "aaabbccddd"
# Output: "a3b2c2d3"
```

'''


def run_length_encode(s):
    if not s:
        return ""

    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1

    # Add the last group
    result += s[-1] + str(count)
    return result

# Test
s = "aaabbccddd"
print(run_length_encode(s))  # Output: "a3b2c2d3"

