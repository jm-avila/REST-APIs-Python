# colect keyword arguments into a dictionary
def example_1(**kwargs):
    print("example_1", kwargs)

example_1(name="Bob", age=25)
print()

# unpack dictionary into keyword arguments
def example_2(name, age):
    print("example_2", name, age)

details = {"name": "Bob", "age": 25}

example_1(**details)
example_2(**details)
print()

# **kwargs colect keyword arguments into a dictionary.
# The dictionary is then passed to example_1 func.
def example_3(**kwargs):
    print("example_3")
    example_1(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

# the details dictionary is passed as keyword parameters to example_3 func.
example_3(**details)
example_3(name="Bob", age=25)

# *args unnamed arguments are colected in a tuple
# **kwargs named arguments are colected in a dictionary

def example_4(*args, **kwargs):
    print(args)
    print(kwargs)

example_4(1, 3, 5, name="Bob", age=25)