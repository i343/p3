# import module
import contextvars

# declaring the variable 
# to it's default value
cvar = contextvars.ContextVar("cvar", default = "test1")

print("1 value of context variable cvar: \n", cvar.get())

# calling set method
token = cvar.set("test2")

print("\n2 value after calling set method: \n", cvar.get())

# checking the type of token instance
print("\n3 Type of object instance returned by set method: \n", type(token))

# calling the reset method.
cvar.reset(token)

print("\n4 value after calling reset method: \n", cvar.get())