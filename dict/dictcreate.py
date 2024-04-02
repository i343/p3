# A dictionary in Python is a data structure that stores the value in key:value pairs.
# https://www.geeksforgeeks.org/python-dictionary/
Dict0 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict0)



# dictionary can be created by placing a sequence of elements within curly {} braces, separated by a ‘comma’.
Dict1 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict1)


Dict2 = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict2)

# Different Ways to Create a Python Dictionary

Dict4 = {}
print("Empty Dictionary: ")
print(Dict4)

Dict5 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict5)

Dict6 = dict(
    [
        (1, 'Geeks'), 
        (2, 'For'),
     ])
print("\nDictionary with each item as a pair: ")
print(Dict6)

# Nested Dictionaries

Dict7 = {
    1: 'Geeks', 
    2: 'For', 
    3: 
    {
        'A': 'Welcome', 
        'B': 'To', 
        'C': 'Geeks'
        }
        }

print(Dict7)

# Adding Elements to a Dictionary
#  Add Items to a Python Dictionary with Different DataTypes
print("start Dict67 -=============================")

Dict67 = {}
print("Empty Dictionary: ")
print(Dict67, "0")
Dict67[0] = 'Geeks'
Dict67[2] = 'For'
Dict67[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict67, "1 +3")

Dict67['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict67, "2 +1")

Dict67[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict67, "3 =2 ")

Dict67[5] = {'Nested': 
             {
                 '1': 'Life', 
                 '2': 'Geeks'
                 }
                 }
print("\nAdding a Nested Key: ")
print(Dict67, "4 +5")

# Access a Value in Python Dictionary

Dict33 = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print("Accessing a element using key:")
print(Dict33['name'])
print(Dict33.get(1), "name")
print("Accessing a element using key:")
print(Dict33[3], "[]")
print(Dict33.get(3), "get")

del(Dict33[1]) 
print("Data after deletion Dictionary=")
print(Dict33)

print("start Dict33 -=============================")

# Accessing an Element of a Nested Dictionary

Dict44 = {
    'Dict1': {1: 'Geeks'},
    'Dict2': {'Name': 'For'}
    }
 
print(Dict44['Dict1'], "dict44")
print(Dict44['Dict1'][1], "dict44")
print(Dict44['Dict2']['Name'], "dict44")


print("start Dict1 and Dict2 -=============================")

dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
dict2 = dict1.copy()

print(dict1, "dict1 - start")
print(dict2, "dict2 - copy")

dict1.clear()
print(dict1, "dict1 clear")
print(dict2.get(1), "dict2 get")
print(dict2.items(), "dict2 items")
print(dict2.keys(), "dict2 keys")
dict2.pop(4)
print(dict2, "dict2 -pop")
dict2.popitem()
print(dict2, "dict2 -popitem")
dict2.update({3: "Scala"})
print(dict2, "dict2 update" )
print(dict2.values(), "dict2 values")