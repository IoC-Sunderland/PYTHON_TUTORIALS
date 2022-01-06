# The use of Inheritance in Python OOP
Inheritance is the ability to derive both ***attributes*** and ***methods*** from one **Class** to another. 

This enables us to re-use code and improve readability.

The most basic example of Inheritance in action is the Parent and Child relationship.

**Example:**

Let's say we have a basic class called **Parent** (below):
```
class Parent:
    def __init__(self):
        self.foo = "foo"
        self.bar = "bar"
```
**Parent** has two attributes ***foo*** and ***bar*** intialised to ***"foo"*** and ***"bar"*** respectively.

Now, let's create another class called **Child** (below):
```
class Child(Parent):
    pass
```
Notice how the word **Parent** here is placed inside parentheses when defining the **Child** class.

This is how we implement **Inheritance** in Python. We are telling Python that the **Child** class ***inherits*** from the **Parent** class.

Let's see an example of what inheritance has done in the **Child** class by creating an instance of **Child** and attempting to access the inherited attributes:

```
c1 = Child() # Instance of Child class
print(c1.foo) # "foo"
print(c1.bar) # "bar"
```
We should get:
```
>>> foo
>>> bar
```
**Question:** But how were we able to access attributes from the Child instance when inside the Child class we simply have:
```
class Child(Parent):
    pass
```
**Answer:** ***Inheritance!***

The **Child** class has inherited all of the **Parent** classes attributes automatically.

This may seem trivial now but if the Parent class has many more lines of code then implementing inheritance will save time and also reduce the possibility of human errors  creeping in.

**Question:** *What about methods?*

Let's go back to our **Parent** class (below):

```
class Parent:
    def __init__(self):
        self.foo = "foo"
        self.bar = "bar"
    
    def test(self):
        return "Hi from Parent's test() method!"
```
Here we have added the **test()** method to the **Parent** class which simply returns the string ***"Hi from Parent's test() method!"***.

Now, we can call the **test()** method from our **Child** instance:

*Note: Since the Parent class has been altered it will need to be saved and run again to take effect*

```
c1.test()
```

This will give us:
```
Hi from Parent's test() method!
```
Again, through the use of ***Inheritance*** we have given the Child class the ability to call a method defined solely in the Parent class.

