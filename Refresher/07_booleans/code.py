# Comparisons: ==, !=, >, <, >=, <=
print("5 == 5", 5 == 5)
print("5 != 5", 5 != 5)
print("5 > 4 ", 5 > 4)
print("5 < 4 ", 5 < 4)

print()
# is, compares if the are the same not if they are equal
print("5 is 5", 5 is 5)

l1 = ["Rolf", "Dan"]
l2 = ["Rolf", "Dan"]
l3 = ["Dan", "Rolf"]
l4 = l3
print("l1 is l2", l1 is l2)
print("l3 is l4", l3 is l4)

l4.append("Cam")
print("l3",l3)
