

class ClassTest:
    # instance method, belongs to an instance of a class and receives the instance as implicit first argument.
    # are used to access the values of an instance.
    def instance_method(self):
        print(f"Called instance_method of {self}")

    # class method, belongs to a class can be called by the class or an instance of the class and receives the class as implicit first argument.
    # are used to access the class itself, for example factories.
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    # static method, belongs to a class can be called by the class annd instances and does not receive an implicit first argument.
    # are used to place functions that have a relationship with the class but don't need the instance or class.
    @staticmethod
    def static_method():
        print(f"Called static_method")

print("Instance Example")
test = ClassTest()
test.instance_method()
test.class_method()
test.static_method()
print()

print("Class Example")
ClassTest.class_method()
ClassTest.static_method()

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)

harryPotterHardcover = Book.hardcover("Harry Potter", 1500)
harryPotterPaperback = Book.paperback("Harry Potter", 1500)
print(harryPotterHardcover)
print(harryPotterPaperback)