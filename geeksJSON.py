# Python program to update
# JSON
# https://www.geeksforgeeks.org/append-to-json-file-using-python/

import json

# Example 1: Updating a JSON string.
 
# JSON data:
x = '{ "organization":"GeeksForGeeks",  "city":"Noida", "country":"India"}'

# python object to be appended
y = {"pin":110096}

# parsing JSON string:
z = json.loads(x)

# appending the data
z.update(y)

# the result is a JSON string:
print(json.dumps(z))
print(json.dumps(z, indent=2))

# https://www.geeksforgeeks.org/python-difference-between-json-dump-and-json-dumps/?ref=ml_lbp


# Python program to convert 
# Python to JSON 
	
		
# Data to be written 
dictionary = { 
            
"id": "04", 
"name": "sunil", 
"department": "HR"
} 	
# Serializing json 
json_object = json.dumps(dictionary, indent = 4) 
print(json_object)

# Python program to write JSON
# to a file



# Data to be written
dictionary = {
	"name" : "sathiyajith",
	"rollno" : 56,
	"cgpa" : 8.6,
	"phonenumber" : "9976770500"
}

print(json.dumps(dictionary)) 
print(json.dumps(dictionary, indent = 4)) 

with open("p3/sample1.json", "w") as outfile:
	json.dump(dictionary, outfile)
print("sample1 - Done.")
 
with open("p3/sample2.json", "w") as outfile:
	json.dump(dictionary, outfile, indent=4)
print("sample2 - Done.")

#Python – Pretty Print JSON

json_data = '[ {"studentid": 1, "name": "ABC", \
                "subjects": ["Python", "Data Structures"]}, \
				{"studentid": 2, "name": "PQR",\
				"subjects": ["Java", "Operating System"]} ]'
obj = json.loads(json_data)
json_formatted_str = json.dumps(obj, indent=4)
print(json_formatted_str)

data3 = [{"studentid": 1, "name": "ABC", 
		"subjects": ["Python", "Data Structures"]},
		{"studentid": 2, "name": "PQR", 
		"subjects": ["Java", "Operating System"]}]

print(json.dumps(data3)) 
print(json.dumps(data3, indent = 3)) 

fileNameData3 = "p3/sample_data3.json"

with open(fileNameData3, "w") as write_file_data3:
	json.dump(data3, write_file_data3, indent=3)
print("sample_data3 write. Done.")

with open(fileNameData3, "r") as read_file_data3:	
	obj_data3 = json.load(read_file_data3)

print(json.dumps(obj_data3, indent=2))

print("sample_data3 read. Done.")