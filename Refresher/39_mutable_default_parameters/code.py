from typing import List, Optional

class Student:
    def __init__(self, name: str, grades: List[int] = []): # avoid mutable default parameters.
        self.name = name
        self.grades = grades
    
    def take_exam(self, result: int):
        self.grades.append(result)

bob = Student("Bob")
bob.take_exam(90)

rolf = Student("Rolf")

# bob and rolf are sharing the same default grades list
print("bob", id(bob.grades), bob.grades)
print("rolf", id(rolf.grades), rolf.grades)
print(bob.grades == rolf.grades)

class Student2:
    def __init__(self, name: str, grades: Optional[List[int]] = None): # correct pattern
        self.name = name
        self.grades = grades or [] # if no list is passed, each instances que it's own list
    
    def take_exam(self, result: int):
        self.grades.append(result)

bob = Student2("Bob")
bob.take_exam(90)

rolf = Student2("Rolf")

# bob and rolf aren't sharing the same default grades list
print("bob", id(bob.grades), bob.grades)
print("rolf", id(rolf.grades), rolf.grades)
print(bob.grades == rolf.grades)