import os

print("start!")
osLoginGet = os.getlogin()

print("os: ", osLoginGet)

nameLogin = osLoginGet
inputLoginStr = 'Input login ['+nameLogin+'] '
inputLoginGet = input(inputLoginStr)
if inputLoginGet != "": nameLogin = inputLoginGet
print("login: ",nameLogin)

