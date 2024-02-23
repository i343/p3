import sys
import time


# def timed_input(caption, timeout=5):
#     def echo(c):
#         sys.stdout.write(c)
#         sys.stdout.flush()        

#     echo(caption)

#     _input = []
#     start = time.monotonic()
#     while time.monotonic() - start < timeout:
#         if msvcrt.kbhit():
#             c = msvcrt.getwch()
#             if ord(c) == 13:
#                 echo('\r\n')
#                 break
#             _input.append(c)
#             echo(c)

#     if _input:
#         return ''.join(_input)


# ch = sys.stdin.read(5)

vvodData = sys.stdin.read(5)

for line in vvodData:
    if 'Ex' == line.rstrip():

        break 
    print(f'Processing Message from sys.stdin ***** {line}')

print("Done")

import readline

while True:
    response = input("> ").strip()

    if response.lower() == "quit":
        break

    print(f"You entered '{response}'")