# 1. str(dic) :- This method is used to return the string, denoting 
# all the dictionary keys with their values.
# 2. items() :- This method is used to return the list with 
# all dictionary keys with values.

# Python code to demonstrate working of 
# str() and items() 
  
# Initializing dictionary 
dic1 = { 'Name' : 'Dini', 'Age' : 19 } 
dic2 = { 'Name' : 'Nan', 'Age' : 22, 'id': 1234 } 
  
# using str() to display dic as string 
print ("The constituents of dictionary as string are : ") 
str1 = str(dic1)
print (str1, str1[0:5:1], str1[0:7:3])

dict2 = dic1.copy()
str2 = str(dict2)  
print (str2, str2[0:1:1], str1[0:-1:-1])

# using str() to display dic as list 
print ("The constituents of dictionary as list are : ") 
print (dic1.items()) 
print (dict2.items()) 

dict2.clear()
print (dict2.items()) 

dic1.update(dic2)

print (dic1.items()) 

# Initializing dictionary 
dic3 = { 'Name' : 'Nandini', 'Age' : 19, 'ID' : 2541997 } 
  
# Initializing list 
li3 = [ 1, 3, 5, 6 ] 
  
  
# using type() to display data type 
print ("The data type of dic is : ",end="") 
print (type(dic3), len(dic3), "dic3") 
  
# using type() to display data type 
print ("The data type of li is : ",end="") 
print (type(li3), len(li3), "li3" )

