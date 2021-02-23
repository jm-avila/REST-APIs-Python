# lambda functions are anonymous functions normaly used to return values
lambda x, y: x + y
add = lambda x, y: x + y

print(add(5,5))

print((lambda x, y: x + y)(5, 5))

def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
doubled_1 = [x * 2 for x in sequence]
doubled_2 = [double(x) for x in sequence]
doubled_3 = [(lambda x: x * 2)(x) for x in sequence]
doubled_4 = map(lambda x: x * 2, sequence)
doubled_5 = map(double, sequence)

print("doubled_1", doubled_1)
print("doubled_2", doubled_2)
print("doubled_3", doubled_3)
# Maps are lazily evaluated, values are only computed on-demand.
print("doubled_4", list(doubled_4))
print("doubled_5", list(doubled_5))