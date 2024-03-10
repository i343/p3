import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
# y = json.loads(x)
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])


# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x, indent=1)

# the result is a JSON string:
print(y)

y = json.dumps(x, indent=2)
print(y)

y = json.dumps(x, indent=3)
print(y)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4))

print(json.dumps(x, indent=3, separators=(". ", " = ")))
print(json.dumps(x, indent=3, sort_keys=True))
print(json.dumps(x, indent=3))