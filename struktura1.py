s = "Hello, " 
t = "World." 
u = s+ t 
print(type(u)) 
print(u) 
print(u[9])

n = str(9876) 
print(n[2], n, "n")

L = [1,2,3,4,5,6]
print(type(L))
print(L, "L1")

L.append(100)
print(L, "L2")
print("The first item is", L[0]) 
print("The second item is", L[1]) 
print("The last item is", L[-1]) 
print("The second to last item is", L[-2])

L[2] = 7 
L[3] = 33 
L[4] = 2 
L[-2] = 99
print(L, "L2")

t = (1, 2, "skip a few", 99, 100)
print(type(t)) 
print(t, "t") 
print(t[4], "t")

d = dict()
d[5] = 'five'
d[2] = 'two' 
d['pi'] = 3.1415926
print(d, "d") 
print(d['pi'], "d_pi")

s = {2,1} 
print(type(s)) 
s.add(3) 
s.add(2) 
s.add(2) 
s.add(2) 
print(s)

a = "a string"
b = ["my", "second", "favorite", "list"] 
c = (1, "tuple")
d = {'a': 'b', 'b': 2, 'c': False}
e = {1,2,3,4,4,4,4,2,2,2,1}
print(len(a), len(b), len(c), len(d), len(e))

a = "a string"
b = ["my", "second", "favorite", "list"] 
c = (1, 2, 3, "tuple")
print(a[3:7])
print(a[1:-2])
print(b[1:])
print(c[:2])

mylist = [1,3,5]
mytuple = (1, 2, 'skip a few', 99, 100) 
myset = {'a', 'b', 'z'}
mystring = 'abracadabra'
mydict = {'a': 96, 'b': 97, 'c': 98}

for item in mylist: 
    print(item)

for item in mytuple:
    print(item)

for element in myset: 
    print(element)

for character in mystring: 
    print(character)

for key in mydict: 
    print(key)

for key, value in mydict.items(): 
    print(key, value)

for value in mydict.values(): 
    print(value)

for i in range(5): 
    j = 10 * i + 1
    print(j, end=' ')