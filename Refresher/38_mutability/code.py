a = []
b = a

# id gives you the location in memory
print(id(a))
print(id(b))
print(a == b)

a.append("a")
b.append("b")

print(a)
print(b)

# in python most values are mutable.

# tuples, strings, integers and booleans are no mutable.