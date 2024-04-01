# Python3 code to remove whitespace
# Remove Spaces from a String in Python
#
#
# Using replace() 
# Using translate() 
# Using lstrip() function
# Using rstrip() function
# Using isspace() method
# Using Regex and itertools
# Using split() and strip() function
# Using NumPy

def remove1(string:str) -> str:
    return string.replace(" ", "").replace("\n","")

# don`t work
def remove2(string:str) -> str:
    table2_dict = {
        ord(' ') : None,
        ord(',') : None,  
        ord('.') : None,  
        ord('!') : None,  
        '\n'     : '',  
        '\t'     : '2',  
        '\r'     : '3',  
        }
    table2 = str.maketrans(table2_dict)
    return string.translate(table2)

 
# Driver Program
string0 = ' g e e       \nk\n'



# Remove Whitespace from String using Replace()
print(string0, "resplace") 
print(remove1(string0),"replace")
 
 
# Remove Whitespace from String using Translate() 
print(string0, "translate") 
print(remove2(string0),"translate")

# Remove Whitespace from String using lstrip() function

string1 = "www.geeksforgeeks.org www."
 
string_new1 = string1.lstrip("w.")
print(string1, "lstrip") 
print(string_new1, "lstrip")

# Delete Whitespace from String using rstrip() function

# string = "www.geeksforgeeks.org www."
 
string_new2 = string1.rstrip("w.")
 
print(string1, "rstrip") 
print(string_new2, "rstrip")

# Trim Extra Spaces from String using isspace() method

def remove3(string):
    ns=""
    for i in string:
        if(not i.isspace()):
            ns+=i
    return ns
    
print(string0, "isspace")
print(remove3(string0), "isspace")


# Remove Whitespace from String using Regex and itertools

import re
import itertools
 
def remove4(string):
    
    pattern = re.compile(r'\s+')
    
    string = re.sub(pattern, '', string)
    
    resList = list(itertools.filterfalse(lambda x: x == ' ', string))
    
    return ''.join(resList)
 
print(string0, "regex + intertools")
print(remove4(string0), "regex + intertools")

# Remove Whitespace from String using split() function

string22 = string0

print(string0, "split")
map_string22 = map(lambda x: x.strip(), string22.split())
print(map_string22, "split")
list_string22 = list(map_string22)
print(list_string22, "split")
string22 = ''.join(list_string22)
 
print(string22, "split")

# Trim Blank Spaces from String using NumPy

# import numpy as np
 
# def remove(string):
#     return np.char.replace(string, ' ', '')
 
# print(remove(string0))

# Python String | strip()
string111 = '   Geeks for Geeks   '
 
print(string111, "strip")
 
# Leading spaces are removed
print(string111.strip(), "strip")
 
# Geeks is removed
print(string111.strip('   Geeks'), "strip")
 
# Not removed since the spaces do not match
print(string111.strip('Geeks'), "strip")

string222 = '@@@@Geeks for Geeks@@@@@'
print(string222, "strip")
 
# Strip all '@' from beginning and ending
print(string222.strip('@'), "@ strip")
 
string24 = 'www.Geeksforgeeks.org'
 
# '.grow' removes 'www' and 'org' and '.'
print(string24.strip('.grow'), "grow strip")

# Python code to check for identifiers
def Count33(string):
 
    print("Length before strip():", end="")
    print(len(string))
 
    # Using strip() to remove white spaces
    strCount = string.strip()
    print("Length after removing spaces:", end="")
    print(len(strCount))
    return strCount
 
# Driver Code
string33 = "  Geeks for Geeks   "
print(string33, "len")
print(Count33(string33), "len")


# Purpose of the Python Strip() Function

my_string = "   Hello, \n world!  \n "
print(my_string, "strip 158")
stripped_string = my_string.strip() 
print(stripped_string, "strip 160") 

print(string0, "strip 36")
new_string0 = string0.strip()
print(new_string0, "strip 36")

# Python Stripping String with Strip() function 
string55 = """    geeks for geeks    """ 
  
# prints the string without stripping 
print(string55, "strip 169")  
  
# prints the string by removing leading and trailing whitespaces 
print(string55.strip(), "strip 169")    
  
# prints the string by removing geeks 
print(string55.strip(' geeks'), "strip 169")

# Python Program to demonstrate use of strip() method  
  
str1 = 'geeks for geeks'
# Print the string without stripping. 
print(str1, "strip 181") 
  
# String whose set of characters are to be 
# remove from original string at both its ends. 
str2 = 'ekgs'
  
# Print string after stripping str2 from str1 at both its end. 

# neponyav
print(str1.strip(str2), "strip 181")

string44 = "\nHello, World!\n"
print(string44, "strip 194")
new_string = string44.strip() 
print(new_string, "strip 194")

# Python3 program to demonstrate the practical application 
# strip()  
  
string55 = " the King has the largest army in the entire world the" 
print(string55, "strip 204")
  
# strip function works on characters and removes characters till it sees,  
# the last or beginning characters mentioned in the function has been removed 
print(string55.strip(" hte"), "strip 204")