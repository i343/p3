# Using Inbuilt sum() Function
# Python3 Program to find sum of all items in a Dictionary

def returnSum0( myDict:dict ) -> int:
	list1 = []
	for index_myDict in myDict:
		index_field = myDict[index_myDict]
		list1.append(index_field)
		print(index_myDict, index_field, "09")
	print(list1, "10")
	final = sum(list1)
	return final

# Driver Function
dict0 = {'a': 100, 'b': 200, 'c': 300}
print("Sum1 :", returnSum0(dict0))

# Using For loop to iterate through values using values() function
# Python3 Program to find sum of all items in a Dictionary
# Function to print sum


def returnSum1(dict1:dict) -> int:
	sum = 0
	lenSum = 0
	for i in dict1.values():
		len_i = len(str(i))
		print(i, "26", len_i)
		sum = sum + i
		lenSum = lenSum + len_i
	print( sum, lenSum, "31")
	return sum

# Driver Function
# dict1 = {'a': 100, 'b': 200, 'c': 300}
print("Sum2 :", returnSum1(dict0))

# Python3 Program to find sum of
# all items in a Dictionary

def returnSum2(dict):
	sum = 0
	for i1 in dict:
		index_dict = dict[i1]
		print(i1, index_dict, "42")
		sum = sum + index_dict
	return sum

# Driver Function
# dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum3 :", returnSum2(dict0))

# Using values() and sum() function

# Python3 Program to find sum of
# all items in a Dictionary

# Function to print sum


def returnSum3(dict):
	print(dict.values(), "58")
	return sum(dict.values())

# Driver Function
print("Sum4 :", returnSum3(dict0))

# Using the lambda function

import functools

sum_dic = functools.reduce(lambda ac,k: ac+dict0[k], dict0, 0)

print("Sum5 :", sum_dic)

# Using a generator expression and the built-in sum function

def returnSum(myDict):
	return sum(myDict[key] for key in myDict)

print("Sum6 :", returnSum(dict0))

#This code is contributed by Edula Vinay Kumar Reddy
# Using the reduce() function 


def sum_dict_values(dict):
    return functools.reduce(lambda acc, x: acc + dict[x], dict, 0)
 
# Driver Function
print("Sum7 :", sum_dict_values(dict0))