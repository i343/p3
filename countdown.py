# countdown.py

from time import sleep

for second in range(3, 0, -1):
    print(second)
    sleep(1)
print("Go!")

for second in range(3, 0, -1):
    print("\r" , str(second) , end=" ")
    sleep(1)
print("\r Go!")

for second in range(3, 0, -1):
    print("\b\b\b" , str(second), end=" ")
    sleep(1)
print("\b\b\b" , "Go!")