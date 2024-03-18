import os
import pwd

print("start!")
osLoginGet = os.getlogin()

print("os get login ->", osLoginGet)

nameLogin = osLoginGet
inputLoginStr = 'Input login ['+nameLogin+'] '
inputLoginGet = input(inputLoginStr)
if inputLoginGet != "": nameLogin = inputLoginGet
print("login -> ",nameLogin)

print("path user ->", os.path.expanduser('~'))
print("get uid ->", os.environ.get('UID'))
print("get user ->", os.environ.get('USER'))
print("get logname ->", os.environ.get('LOGNAME'))
print("get username ->", os.environ.get(' USERNAME'))
# print(os.environ.items())

# Print the real user ID of the current process 
print("get uID ->", os.getuid()) 
print("get pw id ->",pwd.getpwuid(os.getuid())[0])
# print(pwd.getpwuid(os.getuid()))