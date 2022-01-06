# Define an empty Python list
l = []

# Add an element of type Integer to list
l.append(1)

# Check contents of list
print(l) # [1]

# Check length of list
print(len(l)) # 1

# Add another Integer element
l.append(2)

# Check contents of list
print(l) # [1, 2]

# Check length of list
print(len(l)) # 2

# Add another element of type String
l.append("Three")

# Check contents of list
print(l) # [1, 2, 'Three']

# Check length of list
print(len(l)) # 3

# Get element at particular index
# Remember, lists begin at index 0
print(l[0]) # 1
print(l[1]) # 2
print(l[2]) # Three

# Slicing the list up
# Remember, slicing gives elements up to but not including last element
# Example: l[0:1] gives all elements fromindex 0, up to BUT NOT INCLUDING index 1
print(l[0:1]) # [1]

# No second index provided? Will return all elements
print(l[0:]) # [1, 2, 'Three']

# Removing elements with:

# Pop - Always removes the last element in list
l.pop()
print(l) # [1, 2]

# Remove - Remove element provided in parentheses
l.remove(1)
print(l) # [2]

# What if no element at given index
print(l[1]) # Error!