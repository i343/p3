# Sort Python Dictionaries by Key or Value
# Sorting Dictionary By Key
from collections import OrderedDict, defaultdict
import sys

myDict0 = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}

print(myDict0, "<- myDict0") 

list_keys = myDict0.keys()
print(list_keys, "<- list_keys")

myKeys0 = list(list_keys)
print(myKeys0, "<- myKeys0 not sort")


myKeys0.sort()
print(myKeys0, "<- myKeys0 sort")


sorted_dict0 = {i: myDict0[i] for i in myKeys0}
print(sorted_dict0, "<- sorted_dict0")

key_value = {}

# Initializing value
key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323
# Displaying the Keys in Sorted Order 

# Function calling
def dictionary() -> str:
    # Declare hash function
  
    print("key_value", key_value, "d0")
 
    # iterkeys() returns an iterator over the
    # dictionary’s keys.    
    print("key_value.keys")

    for i1 in sorted(key_value.keys()):
        print(i1, end=" ")
    print("d1")

    print("key_value.items")
    for i2 in sorted(key_value.values()):
        print(i2, end=" ")
    print("d2")

    # Sorting the Keys and Values Alphabetically Using the Key
    # sorted(key_value) returns a sorted list
    # of the Dictionary’s keys.
    for i3 in sorted(key_value):
        print((i3, key_value[i3]), end=" ")
    print("d3")

    # Sorting the Keys and Values Alphabetically Using the Value
   # Note that it will sort in lexicographical order
    # For mathematical way, change it to float
    print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])),"d4")
    print(sorted(key_value.items(), key=lambda kv0: (kv0[0], kv0[1])),"d5")

    # Python Program to Handling Missing keys in Python Dictionaries Using key
    key_if = 7
    if key_if in key_value:
        print("key =", key_value[key_if], "get1")
    else:
        print(key_if, "<- key not found get1")

    # Python Program to Handling Missing keys in Dictionaries Using get()
    print(key_value.get(key_if, 'Not found'), "num1 - get2")
    print(key_value.setdefault(key_if, 88), "num2 - get2")
    print(key_value.get(key_if, 'Not found'), "num3 - get2")

    # Handling Missing keys in Python Dictionaries Using setdefault()
    print(key_value.get(str(key_if), 'Not found'), "str1 - get2")
    print(key_value.setdefault(str(key_if), 99), "str2 - get2")
    print(key_value.get(str(key_if), 'Not found'), "str3 - get2")

    # Python Program to Handling Missing keys in Python Dictionaries Using defaultdict
    # Python code to demonstrate defaultdict
    
    # declaring defaultdict
    # sets default value 'Key Not found' to absent keys

    defd0 = defaultdict(lambda : 'Key Not found')

    # initializing values 
    defd0["a"] = '1'
    defd0["b"] = "2"
    
    # printing value 
    print ("The value associated with 'a' is : ",end="")
    print (defd0['a'])
    
    # printing value associated with 'c'
    print ("The value associated with 'c' is : ",end="")
    print (defd0['c'])

    return "Done! d6"
 
 
print(dictionary())


# Sorting the dictionary by key 
# Creates a sorted dictionary (sorted by key)
 
dict0 = {'ravi': '10', 'rajnish': '9',
        'sanjeev': '15', 'yash': '2', 'suraj': '32'}

dict1 = sorted(dict0.items())
dict3 = OrderedDict(dict1)
dict4 = sorted(dict0.keys())


print(dict0, "0")
print(dict1, "1")
print(dict3, "3")
print(dict4, "4")

# Ways to sort list of dictionaries by values in Python – Using lambda function
# Python code demonstrate the working of
# sorted() with lambda

# Initializing list of dictionaries
list99 = [
    {"name": "Nandini", "age": 21},
	{"name": "Manjeet", "age": 20},
	{"name": "Nikhil", "age": 19},
    ]

print("_______________________________________________________")
print(list99, 'list99')

# using sorted and lambda to print list sorted
# by age
print("The list printed sorting by age: ")
print(sorted(list99, key=lambda i: i['age']))

print("\r")

# using sorted and lambda to print list sorted
# by both age and name. Notice that "Manjeet"
# now comes before "Nandini"
print("The list printed sorting by age and name: ")
print(sorted(list99, key=lambda i: (i['age'], i['name'])))

print("\r")

# using sorted and lambda to print list sorted
# by age in descending order
print("The list printed sorting by age in descending order: ")
print(sorted(list99, key=lambda i: i['age'], reverse=True))

# Ways to sort list of dictionaries by values in Python – Using itemgetter

# Python code demonstrate the working of sorted()
# and itemgetter

# importing "operator" for implementing itemgetter
from operator import itemgetter

print("_______________________________________________________")

list66 = list99.copy()

print(list66, 'list66')
print(list99, 'list66')

# using sorted and itemgetter to print list sorted by age
print ("The list printed sorting by age: ")
print (sorted(list66, key=itemgetter('age')))

print("\r")

# using sorted and itemgetter to print
# list sorted by both age and name
# notice that "Manjeet" now comes before "Nandini"
print ("The list printed sorting by age and name: ")
print (sorted(list66, key=itemgetter('name','age')))

print("\r")

# using sorted and itemgetter to print list
# sorted by age in descending order
print ("The list printed sorting by age in descending order: ")
print (sorted(list66, key=itemgetter('age'), reverse=True))

print("Size of dic1: " + str(sys.getsizeof(list99)) + "bytes")
print("Size of dic1: " + str(sys.getsizeof(list66)) + "bytes")

print()
# Python dictionary with keys having multiple inputs

# Python code to demonstrate a dictionary
# with multiple inputs in a key.
import random as rn

# creating an empty dictionary
dict78 = {}

# Insert first triplet in dictionary
x, y, z = 10, 20, 30
dict78[x, y, z] = x + y - z;
print(x, "x")
print(dict78, "dict78")
dict78[x] = x + 10
print(dict78[x], "214")
dict78[y] = y + 20
dict78[z] = z + 20 
print(dict78[x], "217")

# Insert second triplet in dictionary
x, y, z = 5, 2, 4
dict78[x, y, z] = x + y - z;

# print the dictionary
print(dict78)

# Python dictionary with keys having multiple inputs to get access to the keys. 

#  dictionary containing longitude and latitude of places
places = {("19.07'53.2", "72.54'51.0"):"Mumbai", \
          ("28.33'34.1", "77.06'16.6"):"Delhi"}
 
print(places)
print('\n')
 
# Traversing dictionary with multi-keys and creating
# different lists from it
lat = []
long = []
plc = []
for i in places:
    lat.append(i[0])
    long.append(i[1])
    plc.append(places[i[0], i[1]])
 
print(lat, "lat")
print(long, "log")
print(plc, "plc")


print("-------------==-----------")

# Python dictionary with keys having multiple inputs
# Creating a dictionary with multiple inputs for keys
data = {
	(1, "John", "Doe"): {"a": "geeks", "b": "software", "c": 75000},
	(2, "Jane", "Smith"): {"e": 30, "f": "for", "g": 90000},
	(3, "Bob", "Johnson"): {"h": 35, "i": "project", "j": "geeks"},
	(4, "Alice", "Lee"): {"k": 40, "l": "marketing", "m": 100000}
}

# Accessing the values using the keys
print(data[(1, "John", "Doe")]["a"])
print(data[(2, "Jane", "Smith")]["f"])
print(data[(3, "Bob", "Johnson")]["j"])

data[(1, "John", "Doe")]["a"] = {"b": "marketing", "c": 75000};
data[(3, "Bob", "Johnson")]["j"] = {"h": 35, "i": "project"};
print(data[(1, "John", "Doe")]["a"]);
print(data[(3, "Bob", "Johnson")]["j"]);
