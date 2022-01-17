# Functions
***Functions*** are used in Python (and other languages) as a way of
modularising code.

By wrapping regularly used code up into a function we can:

    - Reduce human error
    - Re-useable code improves productivity
    - Make our code easier to read (usually!)

We are using ***built-in*** functions all the time:
```
print("Hello") # print() function

input("Enter some input: ) # input() function
```
These handy built-ins mean ***we*** don't have to write the code necessary to accomplish the goals of ***printing to screen*** and ***getting input*** ourselves.

We can of course make our own:
```
# Define the function
def my_function():
    return "My Function!"

# Call the function
my_function() # 'My Function!'
```

And we can add ***arguments***:
```
def my_function(argument1, argument2):
    return argument1 + argument2

my_function("He", "llo") # 'Hello'

```
***Arguments*** are simply parameters we can pass to the function when we call it.

***Arguments*** must be provided when called (or will throw error):
```
my_function() # TypeError: my_function() missing 2 required positional arguments: 'argument1' and 'argument2'
```
Functions may also have a ***return statment*** (this is not mandatory, but commonplace).

The use of a ***return statement*** means we can capture the output of the function for later use:

```
def sum(num1, num2):
    return num1 + num2

total = sum(10, 10)

print(total) # 20
```



A nice, long article with more on functions available [here](https://realpython.com/defining-your-own-python-function/)

