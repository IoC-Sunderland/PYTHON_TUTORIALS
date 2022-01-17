# Lists
**Lists** are a built-in Python data structure.

***Lists*** in other languages are often called ***arrays***.

A Python list is able to hold items of varying types and is ***ordered*** (not to be confused with ***sorted***).

Example:
```
l = ['apples', 'oranges', 'pears']

print(l) # ['apples', 'oranges', 'pears']
```
***Lists*** are mutable:
```
l = ['apples', 'oranges', 'pears']

l.append('bananas') # Add bananas

print(l) # ['apples', 'oranges', 'pears', 'bananas']
```
*Note: ***Tuples*** are similar to lists but are ***immutable****

Accessing items by ***index***:
```
print(l[0]) # apples
print(l[1]) # oranges
print(l[2]) # pears
print(l[3]) # bananas
```
Using a ***for loop***:
```
for item in l:
    print(item)
```
Result:
```
apples
oranges
pears
bananas
```

Removing items:

```
l.pop() # Removes last item - 'bananas'
```
```
l.remove('apples') # By name

print(l) # ['oranges', 'pears']
```
Adding items:

```
l.append('coconuts') # Add to end of list

print(l) # ['oranges', 'pears', 'coconuts']
```

```
l.insert(1, 'cherries') # Insert at given index

print(l) # ['oranges', 'cherries', 'pears', 'coconuts']
```

Sorting the list:
```
print(l) # ['oranges', 'cherries', 'pears', 'coconuts']

l.sort()

print(l) # ['cherries', 'coconuts', 'oranges', 'pears']
```
Checking length of list:
```
len(l) # 4
```

A nice, long article on Lists available [here](https://realpython.com/python-lists-tuples/)