name1 = "Bob"
name2 = "Don"
name3 = "Cat"

greeting1 = f"Hello, {name1}."
template = "Hello, {}."
greeting2 = template.format(name2)
greeting3 = "Hello, %s." % name3

print(greeting1)
print(greeting2)
print(greeting3)