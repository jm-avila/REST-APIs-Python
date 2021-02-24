class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # str is called when converting an object into a string.
    def __str__(self):
        return f"Name: {self.name}, Age:{self.age}"

    # repr is called to create an unambigous representation of an object, is used if str method doesn't exist and by the debbuger.
    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"

bob = Person("Bob", 35)
print(bob)