# Strings
**Strings** are a data type in Python that consists of a sequence of characters.

The following are all examples  of ***strings***:

```
s1 = "Gavin"
s2 = "123"
s3 = "@£$"
s4 = "Gavin123@£$"
```
In Python strings are stored as **Unicode** and encoded as **UTF-8**.

For example, the ***!*** character is represented in **UTF-8(hex)** as ***21***

```
# Create Byte character

c = b'\x21' # The Hex code for ! character

print(c) # b'!'

print(type(c)) # <class 'bytes'>


# Decode using UTF-8

c.decode("UTF-8") # '!'

s = c.decode("UTF-8") 

print(type(s)) # <class 'str'>

```
If you are interested, you can view the all Unicode characters [here](https://www.rapidtables.com/code/text/unicode-characters.html)

And **ASCII** [here](https://www.rapidtables.com/code/text/ascii-table.html)

<br>

# Working with Strings
There are several operations we may want to do on Strings, below are some examples.

**Concatenate** strings together:
```
s1 = "He"
s2 = "llo"

s1 + s2 # 'Hello'
```

Get a character at a specific **index**:
```
s = "12345"

s[0] # 1
s[1] # 2
s[2] # 3
s[3] # 4
s[4] # 5
```
**Loop** through the string:
```
s = "12345"

for character in s:
    print(character)
```
Will output:
```
1                   
2
3
4
5
```

Check length of a string uding ***len()***:
```
s = "12345"
print(len(s)) # 5
```
Capitalise a string:
```
s = "lower"
s.capitalize() # 'Lower'
```
All uppercase:
```
s = "lower"
s.upper() # 'LOWER'
```
All lowercase:
```
s = "UPPER"
s.lower() # 'upper'
```

A nice article can be found [here](https://realpython.com/python-strings/) with more examples of working with strings.