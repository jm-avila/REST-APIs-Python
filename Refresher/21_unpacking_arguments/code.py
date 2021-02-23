# take all arguments pass to the function and makes a tuple with them.
def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total

print(multiply(1, 2, 3))

def add(x, y):
    return x + y

numsList = [3, 5]
# destructure array
print(add(*numsList))

numsDictionary = {"x": 15, "y": 25}
# destructure dictionary when key match the named parameters
print(add(**numsDictionary))

# collects all arguments and take a named argument
def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    else:
        return "No valid operator provided to apply()."

print(apply(1, 2, 3, operator="*"))