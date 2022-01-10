# Polymorphism
Look up the word ***Polymorphism*** online and you will get results like this:

*"the quality or state of existing in or assuming different forms"*

*"the condition of occurring in several different form."*

and even...

*"Polymorphism involves one of two or more variants of a particular DNA sequence"*

**But what has all this got to do with computer science and programming?**

Well, let's start with a simple example using the Python interpreter:

```
>>> 2 + 2
4
```
No surprises there...

How about:

```
>>> "He" + "llo"
'Hello'
```
Interesting, we have used the **+** operator in two different scenarios and it worked in different ways. 

With **integers** provided it added them together and printed the result.

With **strings** provided it concatenated them together and printed the result.

This is ***Polymorphism*** in action!

The **+** operator is taking two different forms depending on what we give it to work with.


## Function Polymorphism
Another example of Polymorphism can be the use of a function that provides different information depending on what type of data we pass it.

```
print(len("Hello")) # String
print(len([1, 2, 3])) # List
print(len({"Name": "Bob"})) # Dictionary

5
3
1
```
When using **len()** function above we get the following:

Data Type: String

Result: Length of String

Data Type: List

Result: Number of items

Data Type: Dictionary

Result: Number of keys

Again, the function behaves differently depending on data type provided, another example of ***Polymorphism***.


## Method Overriding

## Method Overloading
