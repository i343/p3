mylist = []
print(type(mylist)) 
print(isinstance(mylist, list)) 
print(isinstance(mylist, str))

def foo():
    return 0
print(type(foo))

def mygenerator(n): 
    for i in range(n):
        yield i 
        
print(type(mygenerator))
print(type(mygenerator(5)))

class Vector:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
u = Vector(3,4) 
print(u.norm())
print(Vector(5,12).norm())

class Vector0:
    
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    
    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __add__(self, other): 
        newx = self.x + other.x 
        newy = self.y + other.y 
        return Vector0(newx, newy)

u = Vector0(3,4) 
v = Vector0(3,6)
print(u + v, "u + v")

class Vector1:
    
    def __init__(self, x, y):
        try:
            self.x = float(x) 
            self.y = float(y)
        except ValueError: 
            self.x = 0.0 
            self.y = 0.0
            
    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, other):
        newx = self.x + other.x 
        newy = self.y + other.y 
        return Vector1(newx, newy)
    
    def __str__(self):
        return "(%f, %f)" %(self.x, self.y)
        

u1 = Vector1(3,4) 
v1 = Vector1(5,6)
print(u1 + v1, "u1 + v1")

class Diary:
    def __init__(self, title):
        self.title = title 
        self._entries = []
    
    def addentry(self, entry): 
        self._entries.append(entry)
        
    def _lastentry(self):
        return self._entries[-1]

print("-----")    
mydiary = Diary("Don’t read this!!!") 
mydiary.addentry("It was a good day.") 
print("The diary is called ->", mydiary.title)

class MyLimitedList: 
    def __init__(self):
        self._L = []
    def append(self, item):
        self._L.append(item)
    def show(self):
        print(self._L)
    def __getitem__(self, index):
        return self._L[index]

LL = MyLimitedList() 
LL.append(1) 
LL.append(10) 
LL.append(100) 
print(LL[2])
print(LL,"LL")
LL.show()

def duplicates1(L): 
    n = len(L)
    for i in range(n):
        for j in range(n):
            if i != j and L[i] == L[j]: 
                return True
    return False

assert(duplicates1([1,2,6,3,4,5,6,7,8]))
assert(not duplicates1([1,2,3,4]))

import time
for i in range(11): 
    n = 1000
    start = time.time()
    duplicates1(list(range(n)))
    timetaken = time.time() - start
    print("Time taken for n = ", i, n, ": ", timetaken)
    
def timetrials(func, n, trials = 10): 
    totaltime = 0
    for i in range(trials):
        start = time.time() # Таймер должен запускаться здесь. 
        func(list(range(n)))
        totaltime += time.time() - start
    print("average =%10.7f for n = %d" % (totaltime/trials, n))

for n in [50, 100, 200, 400, 800, 1600, 3200]: 
    timetrials(duplicates1, n)
    
def duplicates2(L): 
    n = len(L)
    for i in range(1,n): 
        for j in range(i):
            if L[i] == L[j]: 
                return True
    return False

for n in [1, 10, 20, 40, 80, 160, 320]:
    timetrials(duplicates2, n)
    