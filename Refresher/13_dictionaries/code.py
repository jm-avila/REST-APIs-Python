friends_ages = {"Rolf": 24, "Adam": 30}

friends_ages["Rolf"] = 30

print(friends_ages["Rolf"])

friends = [
    {
        "name": "Rolf",
        "age": 24
    },
    {
        "name": "Adam",
        "age": 30
    },
    {
        "name": "Anne",
        "age": 27
    }
]

print(friends)

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}%")

for student, attendace in student_attendance.items():
    print(f"{student}: {attendace}%")

if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    "Bob is not a student in this class"

attendace_values = student_attendance.values()
print(sum(attendace_values) / len(attendace_values))