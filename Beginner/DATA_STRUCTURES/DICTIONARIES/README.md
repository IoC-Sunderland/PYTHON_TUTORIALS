# Dictionaries
A Python **dictionary** is a data structure that is used to store ***key:value*** pairs.

It is broadly equivalant to a **hashmap** or **hashtable** in other languages.

Historically, **dictionaries** were ***not ordered*** (to improve search speeds).

If you wanted to order a dictionary you could of used an ***OrderedDict***.

*Note: All dictionaries are now ordered in Python since **version 3.6***

Example:

```
my_dict_1 = {'name': 'Gav',
           'age': 21,
           'job': 'Lecturer'}
```
Above dictionary explained:

Name of dictionary: ***my_dict_1***

Keys: ***name***, ***age*** and ***job***

Values: ***'Gav'***, ***21***, ***'Lecturer'***

Each key:value pair is seperated by a comma.

If we want to get all the ***keys***:
```
for i in my_dict_1:
    print(i)
```

If we want to get all the ***values***:
```
for i in my_dict_1:
    print(my_dict_1[i])
```

Both together:
```
for i in my_dict_1:
    print(i, my_dict_1[i])
```

Alternatively:
```
my_dict_1.keys()  # dict_keys(['name', 'age', 'job'])

my_dict_1.values() # dict_values(['Gav', 21, 'Lecturer'])

my_dict_1.items() # dict_items([('name', 'Gav'), ('age', 21), ('job', 'Lecturer')])
```

***Dictionaries*** are mutable
```
# Amend value
my_dict_1["job"] = 'GP'

my_dict_1["job"] # 'GP'
```

```
# Add new key:value pair
my_dict_1["favourite_food"] = "Veggies"
```
A nice, longish article with more examples can be found [here](https://realpython.com/python-dicts/)