x = 5
y = 3.2
z = True
print("x has type", type(x)) 
print("y has type", type(y)) 
print("z has type", type(z))

x = [1, 2, 3] 
y = x
z = [1, 2, 3]
print(x is y) 
print(x is z) 
print(x == z)

x =2
print("x =", x)
print("float(x) =", float(x)) 
print("x still has type", type(x))
print("Overwriting x.")
x = float(x)
print("Now, x has type", type(x))
print(x, "x")

print("сложное")
numstring = "3.1415926"
y = float(numstring)

print("y has type", type(y))
print(y, "y")

best_number = 73
x = str(best_number) 
print("x has type", type(x))
print(x, "x")

thisworks = float("inf")
print("float(\'inf\') has type", type(thisworks)) 
print(thisworks, "thisworks")

infinity_plus_one = float('inf') + 1
print(infinity_plus_one, "infinity_plus_one")
