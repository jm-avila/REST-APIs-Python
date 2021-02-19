friends = ["Rolf", "Jen", "Bob", "Anne"]

for friend in friends:
    print(f"{friend} is my friend.")

for num in range(4):
    print(f"{num + 1}")

grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(f"Grade: {total / amount}")
print(f"Grade: {sum(grades) / amount}")