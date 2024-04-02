# Python program to demonstrate   
# ChainMap   
       
       
from collections import ChainMap   
       
       
d1 = {'a': 1, 'b': 2}  
d2 = {'c': 3, 'd': 4}  
d3 = {'e': 5, 'f': 6}  
    
# Defining the chainmap   
c = ChainMap(d1, d2, d3)   
       
print(c, "d1 d2 d3")

  
# initializing dictionaries 
dic1 = { 'a' : 1, 'b' : 2 } 
dic2 = { 'b' : 3, 'c' : 4 } 
  
# initializing ChainMap 
chain = ChainMap(dic1, dic2) 

print(dic1, "dic1")
print(dic2, "dic2")
print(chain, "chain")

# printing chainMap using maps 
print ("All the ChainMap contents are : ") 
print (chain.maps, "maps") 
  
# printing keys using keys() 
print ("All keys of ChainMap are : ") 
print (list(chain.keys()), "-> 35") 
  
# printing keys using keys() 
print ("All values of ChainMap are : ") 
print (list(chain.values()), "->39") 

# initializing dictionaries 
dic11 = { 'a' : 1, 'b' : 2 } 
dic12 = { 'b' : 3, 'c' : 4 } 
dic13 = { 'f' : 5 } 
  
# initializing ChainMap 
chain4 = ChainMap(dic11, dic12) 
  
# printing chainMap using map 
print ("All the ChainMap contents are : ") 
print (chain4.maps, "51") 
  
# using new_child() to add new dictionary 
chain11 = chain4.new_child(dic13)

# printing chainMap using map 
print ("Displaying new ChainMap : ") 
print (chain11.maps, "58") 
  
# displaying value associated with b before reversing 
print ("Value associated with b before reversing is : ",end="") 
print (chain11['b'], "62") 
  
# reversing the ChainMap 
chain11.maps = reversed(chain11.maps) 
print (chain11.maps, "58") 
  
# displaying value associated with b after reversing 
print ("Value associated with b after reversing is : ",end="") 
print (chain11['b'], "69") 
