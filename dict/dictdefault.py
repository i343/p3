# Python program to demonstrate 
# dictionary 


Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print("Dictionary:") 
print(Dict) 
print(Dict[1]) 

# Uncommenting this print(Dict[4]) 
# will raise a KeyError as the 
# 4 is not present in the dictionary 


# Python program to demonstrate 
# defaultdict 


from collections import defaultdict 


# default_factory: A function returning the default value for the dictionary defined. 
# If this argument is absent then the dictionary raises a KeyError.

def def_value22(): 
    return "Not Present"
      
# Defining the dict 
d22 = defaultdict(def_value22) 
d22["a"] = '1'
d22["b"] = '2'
  
print(d22["a"],"a22") 
print(d22["b"],"b22") 
print(d22["c"],"c22") 
print(d22.__missing__('a'), "a22 - 2") 
print(d22.__missing__('b'), "b22 - 2") 
print(d22.__missing__('c'), "c22 - 2") 
print(d22.__missing__('d'), "d22 - 2") 

# Default_factory: It is a function returning the default value for the dictionary defined. 
# If this argument is absent then the dictionary raises a KeyError.

d44 = defaultdict(lambda: "Not Present") 
d44["a"] = "10"
d44["b"] = "20"
  
print(d44["a"],"a44") 
print(d44["b"],"b44") 
print(d44["c"],"c44") 

# __missing__(): This function is used to provide the default value for the dictionary.

print(d44.__missing__('a'), "a44 - 2") 
print(d44.__missing__('b'), "b44 - 2") 
print(d44.__missing__('c'), "c44 - 2") 
print(d44.__missing__('d'), "d44 - 2") 


# Using List as default_factory

# Defining a dict 
d77 = defaultdict(list) 

for i77 in range(14): 
    d77[i77].append(i77) 
	
print("Dictionary with values as list:") 
print(d77) 

#
# Initializing DefaultDict Objects
# Using int as default_factory

# Defining the dict 
d55 = defaultdict(int) 
   
L55 = [1, 2, 3, 4, 2, 4, 1, 2] 
   
# Iterate through the list 
# for keeping the count 
print(L55, "L55")
for i55 in L55: 
       
    # The default value is 0 
    # so there is no need to  
    # enter the key first 
    print(i55, end= " ")
    d55[i55] += 1
       
print(" i55")
print(d55, "d55")


