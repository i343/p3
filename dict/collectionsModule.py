# Python Collections Module
# Counters
# Initializing Counter Objects

# A Python program to show different 
# ways to create Counter 
from collections import Counter, OrderedDict, defaultdict, ChainMap, namedtuple, deque, UserDict, UserList, UserString 
  
# class collections.Counter([iterable-or-mapping])
# With sequence of items  
counter_sequence = Counter(['B','A','B','C','A','B','B','A','C'])
print(counter_sequence, "0")
  
# with dictionary 
counter_dict = Counter({'A':3, 'B':5, 'C':2})
print(counter_dict, "1")
  
# with keyword arguments
counter_keyword =  Counter(A=3, B=5, C=2, D=0)
print(counter_keyword, "2")

# class collections.OrderDict()
print("This is a Dict:\n") 
d33 = {} 
d33['a'] = 1
d33['b'] = 2
d33['c'] = 3
d33['d'] = 4
    
print('\nBefore Deleting\n')
for key, value in d33.items(): 
    print(key, value, "before33") 
    
# deleting element
d33.pop('a')
print("\n Del \n")
for key, value in d33.items(): 
    print(key, value, "del33") 

# Re-inserting the same
d33['a'] = 1

print('\nAfter re-inserting\n')
for key, value in d33.items(): 
    print(key, value, "after33")



print("\nThis is an Ordered Dict:\n") 
od33 = OrderedDict() 
od33['a'] = 1
od33['b'] = 2
od33['c'] = 3
od33['d'] = 4

print('\nBefore Deleting\n')
for key, value in od33.items(): 
    print(key, value, "before33") 
    
# deleting element
od33.pop('a')
print("\n Del \n")
for key, value in od33.items(): 
    print(key, value, "del33") 

# Re-inserting the same
od33['a'] = 1

print('\nAfter re-inserting\n')
for key, value in od33.items(): 
    print(key, value, "after33")


# Initializing DefaultDict Objects

# Defining the dict 
print("\nDictionary with values as int:") 
d0 = defaultdict(int) 
   
L0 = [1, 2, 3, 4, 2, 4, 1, 2] 
   
# Iterate through the list 
# for keeping the count 
for i0 in L0: 
       
    # The default value is 0 
    # so there is no need to  
    # enter the key first 
    d0[i0] += 1
       
print(d0)

# Defining a dict 
d1 = defaultdict(list) 
  
for i1 in range(6): 
    d1[i1].append(i1) 
      
print("\nDictionary with values as list:") 
print(d1) 

# class collections.ChainMap(dict1, dict2)

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

# Defining the chainmap 
c44 = ChainMap(dict1, dict2, dict3) 
   
print("\n", c44)
# Accessing Values using key name
print(c44['a'])

# Accessing values using values()
# method
print(c44.values())

# Accessing keys using keys()
# method
print(c44.keys())

dict4 = { 'g' : 7 } 
  
# initializing ChainMap 
chain33 = ChainMap(dict1, dict2) 
  
# printing chainMap 
print ("All the ChainMap contents are : ") 
print (chain33, "chain33") 
  
# using new_child() to add new dictionary 
chain1 = chain33.new_child(dict4) 
  
# printing chainMap
print ("Displaying new ChainMap : ") 
print (chain1, "chain1") 

# using new_child() to add new dictionary 

chain2 = chain1.new_child(dict3) 
  
# printing chainMap
print ("Displaying new ChainMap : ") 
print (chain2, "chain2") 

# NamedTuple
# class collections.namedtuple(typename, field_names)

# Declaring namedtuple() 
Student = namedtuple('Student',['name','age','DOB']) 
  
# Adding values 
S0 = Student('Nandini','19','2541997') 
  
# Access using index 
print ("The Student age using index is : ") 
print (S0[0], '0')
print (S0[1], '1')
print (S0[-1], '-1')

  
# Access using name  
print ("The Student name using keyname is : ",end ="") 
print (S0.name)



# 1. _make(): This function is used to return a namedtuple() 
# from the iterable passed as argument.
# 2. _asdict(): This function returns the OrdereDict() as constructed 
# from the mapped values of namedtuple().

# Python code to demonstrate namedtuple() and 
# _make(), _asdict()
  
  
# # Declaring namedtuple() 
# Student = namedtuple('Student',['name','age','DOB']) 
  
# # Adding values 
# S = Student('Nandini','19','2541997') 
  
# # initializing iterable  
li = ['Manjeet', '19', '411997' ] 
  
# initializing dict 
# di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' } 
  
# using _make() to return namedtuple() 
print ("The namedtuple instance using iterable is  : ") 
print (Student._make(li)) 
  
# using _asdict() to return an OrderedDict() 
print ("The OrderedDict instance using namedtuple is  : ") 
print (S0._asdict()) 

# class collections.deque(list)

# Declaring deque
queue4 = deque(['name','age','DOB']) 
  
print(queue4, "queue4")

# initializing deque 
de12 = deque([7,6,1,2,3]) 
  
# using append() to insert element at right end  
# inserts 4 at the end of deque 
de12.append(4) 
  
# printing modified deque 
print ("The deque after appending at right is : ") 
print (de12, "de12 - 0") 
  
# using appendleft() to insert element at right end  
# inserts 6 at the beginning of deque 
de12.appendleft(6) 
  
# printing modified deque 
print ("\nThe deque after appending at left is : ") 
print (de12, "de12 - 0") 


# Removing Elements

# using pop() to delete element from right end  
# deletes 4 from the right end of deque 
de12.pop() 
  
# printing modified deque 
print ("The deque after deleting from right is : ") 
print (de12, "de12") 
  
# using popleft() to delete element from left end  
# deletes 6 from the left end of deque 
de12.popleft() 
  
# printing modified deque 
print ("The deque after deleting from left is : ") 
print (de12)

