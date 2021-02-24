student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student["grades"]))

class Student:
    def __init__(self, name, *grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student_2 = Student("Dany", 90, 90, 93, 78, 90)
student_3 = Student("Rob", 70, 80, 93, 78, 60)

print(student_2.name)
print(student_2.grades)
print(student_2.average())

print(student_3.name)
print(student_3.grades)
print(student_3.average())