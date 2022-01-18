# If/Elif/Else
***If, Elif and Else*** are all ***conditional statements*** in Python.

Conditional statements require a condition to be met in order to execute.

Example:
```
if 10 == 10: # True
    print("Ten is equal to ten!")
```
Result:
```
Ten is equal to ten!
```
Here, the ***if*** statement has a condition to check: **is 10 == (equal to) 10**

If the answer to this question is Yes (***True***) then Python executes the indented code, in this cases it is: **print("Ten is equal to ten!")**

If the answer to the quextion is No (***False***) then the indented code ***is not*** exectued and Python continues to the next line of code:

Example:
```
if 10 == 9: # False
    print("Ten is equal to nine!")
```
Result:
```
```
There is no result as there is no more code for Python to execute, but what if there was?
```
if 10 == 9: # False
    print("Ten is equal to nine!")

print("I will print after if statment has completed!")
```
Result:
```
I will print after if statment has completed!
```

What if we want to trigger some other code if the if statement is ***False***?

```
if 10 == 9: # False
    print("Ten is equal to nine!")
else:
    print("Ten is not equal to nine of course!")
```

Result:
```
Ten is not equal to nine of course!
```

Here, the ***else*** clause triggers and prints the statment.

The ***else*** clause is very useful as it will trigger even if all preceeding statements don't:

```
if 10 == 9: # False
    print("Ten is equal to nine!")
elif 10 == 8:
    print("Ten is equal to eight!")
elif 10 == 7:
    print("Ten is equal to seven!")
else:
    print("None of the above statements were True!")
```

Result:
```
None of the above statements were True!
```
Notice here how I snuck in the use of ***elif***?

We can use ***elif*** to check other conditions and if they are ***True*** execute the indented code:

```
if 10 == 9: # False
    print("Ten is equal to nine!")
elif 10 == 8:
    print("Ten is equal to eight!")
elif 10 == 7:
    print("Ten is equal to seven!")
elif 10 == 10:
    print("Ten is equal to ten!")
else:
    print("None of the above statements were True!")

print("The if/elif/else block has ended!")
```

Result:
```
Ten is equal to ten!The if/elif/else block has ended!

```

As soon as an ***if*** or ***elif*** condition evaluated to  **True** the associated indented code was exectued, then Python left the **if/elif/else** block and continued on.


A nice, shortish article with more examples of if/elif/else (including flowcharts) available [here](https://www.programiz.com/python-programming/if-elif-else)
