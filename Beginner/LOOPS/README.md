# Loops
***Loops*** are useful when we want to ***iterate/loop*** through things.

In Python manhy objects are ***iterables***, meaning we can ***iterate*** through them using loops.

There are two main types of loop in Python:

    - for loop
    - while loop

## **For** loops
The ***for*** loop:

```
s = "Print Me!"

for character in s:
    print(character)
```

Result:

```
P
r
i
n
t

M
e
!
```

Let's make that a bit tidier:
```
s = "Print Me!"

for character in s:
    print(character, end="")

```
Result:
```
Print Me!
```

As you have problably guessed by now ***Strings*** are ***iterable***.

***Lists*** are also iterable:

```
l = [1, 2, 3]

for n in l:
    print(n)
```
Result:
```
1
2
3
```

# While loops
The ***while*** loop:
```
n = 10

while n > 3:
    print(n)
    n = n -1
```
Result:
```
10
9
8
7
6
5
4
```

***While*** loops check a condition, when that condition is **False** the loop terminates.

Let's go back to previous example:
```
n = 10

while n > 9: # Change the condition
    print(n)
    n = n -1
```
Result:
```
10
```
A nice, shortish article on ***for*** loops available [here](https://realpython.com/python-for-loop/)


And...

A nice, shortish article on ***while*** loops available [here](https://realpython.com/python-while-loop/)