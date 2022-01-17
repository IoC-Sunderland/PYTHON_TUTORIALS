from pprint import pprint

# Dictionary (hashmap)
my_dict_1 = {'name': 'Gav',
           'age': 21,
           'job': 'Lecturer'}

my_dict_2 = {'name': 'Sue',
           'age': 30,
           'job': 'Doctor'}

# Print Values
print('>>> my_dict_1.values()')
print(my_dict_1.values())
print('\n')

# Print Keys
print('>>> my_dict_1.keys()')
print(my_dict_1.keys())
print('\n')

# Print Items (Key and Value)
print('>>> my_dict_1.items()')
print(my_dict_1.items())
print('\n')

# Print by index
print('>>> Print by index')
print(my_dict_2['name']) # Sue
print(my_dict_2['age']) # 30
print(my_dict_2['job']) # Doctor
print('\n')

# Iterate through
print('>>> my_dict_1.items()')
for x, y in my_dict_1.items():
  print(x, y)
print('\n')

# Combine dicts into list
combined = [my_dict_1, my_dict_2]

print('>>> combined list')
print(type(combined))
print(combined[0]) # Gav
print(combined[1]) # Sue
print('\n')

print(combined[0]['name']) # Gav
print(combined[0]['age'])  # 21
print(combined[0]['job'])  # Lecturer
print('\n')

# Amend Values
my_dict_2["job"] = 'GP'
print(my_dict_2["job"]) # GP
print('\n')

# Iterate through
print('>>> for loop')
for employee in combined:
    print(employee)
print('\n')   

# Something in dict?
if "Joe" in my_dict_2:
  print("Yes, 'Joe' is one of the keys in the my_dict_2 \
  dictionary")
else:
    print("'Joe' Not Found!")

my_dict_3 = {'name': 'Joe',
           'age': 50,
           'job': 'Farmer'}

combined.append(my_dict_3)
pprint(combined)
print('\n')

for employee in combined:
    if employee['name'] == 'Joe':
        print("Yes, 'Joe' is one of the names in the combined list.")
        print("See below:")
        print(employee['name'], employee['age'], employee['job'])
    else:
        pass

# Nested dicts
employees = {
  "employee_one"   : my_dict_1,
  "employee_two"   : my_dict_2,
  "employee_three" : my_dict_3
}

print(employees)
print('\n')

# Dict() constructor
my_dict_5 = dict(named="Mo", age="23", job='Runner')

print(my_dict_5)