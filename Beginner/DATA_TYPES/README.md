# Data Types

Below are some of Python's built-in data types.

*Note: this list is not exhaustive, but these are the data types you will most likely come across on your Python adventures:*

| Data Type | Description | Example |
| ----------- | ----------- | ------|
| **int**    | Whole number | 100
| **float**  | Floating point number | 10.5
| **str** | Sequence of characters | "Hello"
| **bool**     | True or False value | True
| **list** |  A list/array of mutable values | ['apples', 'oranges', 'pears]
| **tuple** | Similar to list but immutable | ('apples', 'oranges', 'pears')
| **dict** | Stores key:value pairs, mutable |   {"name":"Bob, "age" 21}

**What is mutable/immutable?**
Mutability is the ability to be able change.

If we say something is **mutable** then it can change.

If we say something is **immutable** it can not change.

Example:
```
# Mutable

l = [1, 2, 3] # Lists are mutable
l.pop() # Remove last item
print(l) # [1, 2] # List has changed

s = "Gavin" # Strings are also mutable
s.replace("G", "H") # 'Havin'  
```

```
# Immutable

t = (1, 2, 3) # Tuples are immutable
t.pop() # AttributeError: 'tuple' object has no attribute 'pop'
```

