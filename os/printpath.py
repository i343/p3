#  os.path.join() Function Examples and Uses Cases

import os

# Path
path0 = "/home"

# Join various path components
print(os.path.join(path0, "User/Desktop", "file.txt"))

# Path
path1 = "User/Documents"

# Join various path components
print(os.path.join(path1, "/home", "file.txt"))

# Path
path2 = "/User"

# Join various path components
print(os.path.join(path2, "Downloads", "file.txt", "/home"))


# Base directory and filename
base_dir0 = 'Desktop/Source.github/p3/os'
filename0 = 'printpath.py'

# Construct the full path
full_path0 = os.path.join('/home/r0', base_dir0, filename0)

print(full_path0, "< - 31")

iCounter = 0
# Reading and writing files using the full path
with open(full_path0, 'r') as file:
	content = file.read()
	iCounter +=1
	print(content, iCounter)
	
# Current working directory
current_dir0 = os.getcwd()
print(current_dir0, "42")
# List files in the current directory
files_in_dir0 = os.listdir(current_dir0)
print(files_in_dir0, "45")
# Iterate over files and print their full paths
for file_nameI in files_in_dir0:
	file_path0 = os.path.join(current_dir0, file_nameI)
	print(file_path0)

# List of file names
names = ['UML', 'playS', 'math',  'w3schoolsPython']

# Iterate over file names and process each file
for file_name in names:
	file_path = os.path.join('~/Desktop/Source.github', file_name)
	print(f"Processing file: {file_path}", type(file_path))
	# os.listdir(file_path)

import os.path as path

SETTINGS_FILES_PATHS = [
    path.join(path.dirname(path.realpath(__file__)), "resources/settings.json"),
    '~/.maigret/settings.json',
    path.join(os.getcwd(), 'settings.json'),
]

print(SETTINGS_FILES_PATHS, type(SETTINGS_FILES_PATHS), "SETTINGS_FILES_PATHS")

for indexSET in SETTINGS_FILES_PATHS:
	print(indexSET, "indexSET - 71")
	try:
		os.listdir(indexSET)
	except:
		print("File not found ->", indexSET)

# Using os.path.abspath() to get parent of current directory

# Python program to get parent
# directory 

print("--------------------------\n")

# get current directory
path9 = os.getcwd()
print("Current Directory", path9, "getcwd")

# prints parent directory
ospardir = os.pardir
print(ospardir, "pardir")
ospath99 = os.path.join(path9, ospardir)
print(ospath99, "ospath99")
print(os.path.abspath(ospath99), "ospathabs 94")

# Using os.path.dirname() to get parent of current directory

# Python program to get parent
# directory

print()
# get current directory
path = os.getcwd()
print("Current Directory", path)

# parent directory
parent = os.path.dirname(path)
print("Parent directory", parent)

# Using os.path.relpath() and os.path.dirname()

# Python program to get the
# parent directory


import os.path

# function to get parent
def getParent(path, levels = 1):
	common = path

	# Using for loop for getting
	# starting point required for
	# os.path.relpath()
	for i in range(levels + 1):

		# Starting point
		common = os.path.dirname(common)

	# Parent directory upto specified
	# level
	return os.path.relpath(path, common)

path22 = '/home/r0/Desktop/Source.github/p3/os/printpath.py'
print(getParent(path22, 2))

# Using Path().resolve().parents to get parent of current directory

from pathlib import Path


d = Path(path22).resolve().parents[0]

print(d, ' 143- d')
