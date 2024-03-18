import os
# import pwd

print("start!")

osName = os.name
nameLogin = ""

match osName:
    case "nt":
        print("Windows")
        nameLogin = os.getlogin()
    case "posix":
        print("Unix/MacOS")
        nameLogin = os.environ.get('USER')
    case _:
        print("ОС - невизначено.")

print("os get login ->", nameLogin)

inputLoginStr = 'Input login ['+nameLogin+'] '
inputLoginGet = input(inputLoginStr)
if inputLoginGet != "": nameLogin = inputLoginGet
print("login -> ",nameLogin)

import platform
print("uname -> ", platform.uname())
print("system ->", platform.system())
print("node ->", platform.node())

import socket
print("socet -> ", socket.gethostname())

# print("path user ->", os.path.expanduser('~'))
# print("get uid ->", os.environ.get('UID'))
# print("get logname ->", os.environ.get('LOGNAME'))
# print("get username ->", os.environ.get(' USERNAME'))
# print(os.environ.items())
