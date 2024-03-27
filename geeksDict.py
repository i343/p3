# Example 1 dictionary
sample_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Using the keys() method
keys_list = list(sample_dict.keys())

# Printing the keys
print("Method 1 - Using keys() method:")
print(keys_list)
print()
# Example 2 dictionary

# Iterating through the dictionary and printing keys
print("Method 2 - Iterating through the dictionary:")
for key in sample_dict:
	print(key)
print()

# Example 3 dictionary

# Using list comprehension
keys_list = [key for key in sample_dict]

# Printing the keys
print("Method 3 - Using list comprehension:")
print(keys_list)
print()

# initialize lists for keys and values
keys = ['a', 'b', 'c']
values = [1, 2, 3]

# initialize empty dictionary
dynamic_dict = {}

# dynamically assign key-value pairs using a loop
for i in range(len(keys)):
	dynamic_dict[keys[i]] = values[i]

# print the resulting dictionary
print(1, dynamic_dict)

# create two lists for keys and values

# using dictionary comprehension to create a dictionary
dynamic_dict = {keys[i]: values[i] for i in range(len(keys))}
print(2, dynamic_dict)


# create dictionary dynamically using the zip() function

# creating a dictionary by zipping keys and values together
dynamic_dict = dict(zip(keys, values))
print(3, dynamic_dict)

data = [('a', 1), ('b', 2), ('c', 3), ('a', 4)]
dynamic_dict = {}
# looping through data to populate the dictionary

for key, value in data:
	if key in dynamic_dict:
	# aggregates values if key already exists
		dynamic_dict[key] += value
	else:
	# creates new key if not existing
		dynamic_dict[key] = value
		
print(4,dynamic_dict)
print("*************")

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha", "Resds", "Frsda" ]
roll_no = [ 4, 1, 3, 2, 5, 6 ]

# using zip() to map values
mapped = zip(name, roll_no)

print(1, set(mapped))

names = ['Mukesh', 'Roni', 'Charis']
ages = [24, 50, 18]

for i, (name0, age0) in enumerate(zip(names, ages)):
	print("№",i, name0, age0)
print("----++++---")
zipp22 = zip(name, roll_no)
zipp33 = zip(name, roll_no)

print(type(zipp22))
print("zipp22", zipp22)

enum22 = enumerate(zipp22)
enum33 = enumerate(zipp33)  

print("i0")
for i1, (name2, age2) in enum33:
	print("_N", i1, name2, age2)
print("i1")

print(type(enum22))
print("enum22", enum22)
for i0, (name1, age1) in enum22:
	print("_№", i0, name1, age1)

print("----++++---")

stocks = ['GEEKS', 'For', 'geeks']
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks,
			prices in zip(stocks, prices)}
print(2, new_dict)

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
zipped = zip(tuple1, tuple2)
result = list(zipped)
print(3, result)

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['x', 'y', 'z']
zipped = zip(list1, list2, list3)
print("zipped", zipped)
result = list(zipped)
print(4, result)
print("=====----")

# Define lists for 'persons', 'genders', and a tuple for 'ages'
persons = ["Chandler", "Monica", "Ross", "Rachel", "Joey", "Phoebe", "Joanna"]
genders = ["Male", "Female", "Male", "Female", "Male", "Female", "Female"]
ages = (35, 36, 38, 34)

# Create a zipped object combining the 'persons' and 'genders' 
#lists along with the 'ages' tuple
zipped_result = set(zip(persons, genders, ages))
zipped_result0 = zip(persons, genders, ages)

print(zipped_result, "zipped_result")
# Print the zipped object
print("1 Zipped result as a list:")
for i in list(zipped_result):
    print(i)

print("2 Zipped result as a list:")
for i0 in list(zipped_result):
    print(i0)
