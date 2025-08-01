import contextvars

# declaring the variable
cvar = contextvars.ContextVar("cvar", default = "variable0")

# calling set function to get a token object
token = cvar.set("changed0")

# token.var returns the ContextVar
# object through which token is generated.
print("ContextVar object though which token was generated: ")
print(token.var)

# As only one time set is called
# it should return token.MISSING.
print("\nAfter calling token.old_value : ")
print(token.old_value)

# Recalling set method again to
# test other side of token.old_value
token = cvar.set("changed_2")
print("\nPrinting the value set before set method called last : ")
print(token.old_value)

print("\nThe current value of context variable is : ")
print(cvar.get())