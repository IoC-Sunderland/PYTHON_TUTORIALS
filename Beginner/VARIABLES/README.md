# Variables
***Variables*** are commonly used in programming to store information or state.

They are called ***variables*** because their contents can change or vary.

Example:
```
name = "Gavin"
```
Here, the variable is called ***name*** and the contents of the variable is the string ***"Gavin"***

Example:
```
age = 21
```
Here, the variable is called ***age*** and the contents of the variable is the ***integer*** value **21**.

*Note: The variable name only signifies the content it has no other meaning to Python, i.e. the ***name*** variable could contain an integer and the ***age*** variable could contain a string.*

Example:
```
random_variable_name = 21

x253ythn = "Gavin"
```
These two variable declerations are completely fine in Python but probbaly not very readable to a human so think of this when naming variables (more on this later).

## Using variables
A very simple and valid use case for variables is storing user input for retrieval later.

Example:
```
name = input("Please enter your name: ")
```
Because we have stored the users input in the variable ***name*** we can retrieve it later, perhaps to display a message:
```
print("Hi " + name) # Hi Gav
```

If we don't store the users input in a varibale look what happens:
```
input("Please enter your name: ") # 'Gav'

print("Hi " + name) # NameError: name 'name' is not defined
```
*Note: If you run these code snippets in order, from the Python interpreter, you will not get this error message as you have previoulsy declared the ***name*** variable. Quit the interpreter by typing ***exit()*** and then try again just using the code snippet above.*

Another simple use case could be amending a bank balance:

```
balance = 0

balance = balance + 10 # Make a deposit of 10
```
Here we have taken the existing balance which is **0** and added **10** then reassigned the total to ***balance***.

```
print(balance) # 10
```
Let's try a withdrawal:
```
balance = balance - 5 # Withdraw 5
```
Here we have taken the existing balance which is 10 and subtracted 5 then reassigned the total to ***balance***.
```
print(balance) # 5
```

# Naming Variables
So far we have only used one-word variables like ***name***, ***age*** and ***balance***.

In some scenarios we may want to use longer names with multiple words e.g. ***"user one age"***,  ***"user one name"*** and ***"gavins balance"***.

We can't do this in Python (and most all other languages):
```
user one age = 21 # SyntaxError: invalid syntax
```
To get round this we have two options:

**Option 1: Camel Case**
```
userOneAge = 21
```
Here we have used ***Camel Case*** to create a multiple word variable. ***Camel Case*** is so called because the first letter of each word (not including the first word) is upper-case and so looks like the humps of a camel.

**Option 2: Snake Case**
```
user_one_age = 21
```
Here we have used ***Snake Case*** to create a multiple word variable. Again, think of a snake slithering on the ground and you will understand why it is named this way.

You decide which you prefer!

## Valid/Invalid names
Variable names in Python can be any length and can consist of uppercase and lowercase letters ***(A-Z, a-z)***, digits ***(0-9)***, and the underscore character ***(_)***.

So the following are all ***valid***:
```
x_1 = "Test"
___y_z = "Test"
xyz123_ = "Test"
```
These are ***invalid***:
```
1_x = "Test" # SyntaxError: invalid decimal literal
123_xyz = "Test" # SyntaxError: invalid decimal literal
```
**Why?** Beacuse they both ***start with a digit***.

## Reserved Words or Keywords
Reserved Words or Keywords are words that are reserved for use in the language itself.

For example, the keyword ***def*** is used to define functions in Python (more on functions in another tutorial).

So if we try to create a variable called ***def*** see what happens:
```
def = 10 # SyntaxError: invalid syntax
```
If you want to view a full list of keywords in Python enter the following into the interpreter:
```
help("keywords")
```

A nice, short article is available [here]("https://realpython.com/python-variables/") which covers the above topics with some more examples.

*Note: this article covers ***object references*** but we are not covering this yet, feel free to read this part though as it may help later!*