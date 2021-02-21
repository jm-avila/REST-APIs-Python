# tuple
x = (5, 11)
y = 5, 11

# () are only necesary when python is unable to determine that it's a tuple without them.
x_list = [(5, 11)]

# 
a, b = x

print("x", x)
print("a", a)
print("b", b)

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

print(list(student_attendance.items()))

for t in student_attendance.items():
    print(t)

for student, attendance in student_attendance.items():
    print(student, attendance)

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

bob = people[0]
bobName, _, bobProfession = bob

print(bobName, bobProfession)

# Separate lists

random_numbers = [1,3,2,4,5,9]

head, *body, tail = random_numbers

print(head, body, tail)
print(*body)