# List
friendsList = ["Bob", "Rolf", "Anne"]
print("friendsList: ", friendsList[0], friendsList[1], friendsList[2])
friendsList.append("Caro")
print("friendsList: ", friendsList[3])
friendsList.remove(friendsList[0])
print("friendsList: ", friendsList[0])

print()
# Tuple
# Can't be modified.
friendsTuple = ("Bob", "Rolf", "Anne")
print("friendsTuple: ", friendsTuple[0], friendsTuple[1], friendsTuple[2])

# Set
# Can't be access with brackets notation
# Has no order
# Only holds unique values

friendsSet = {"Bob", "Rolf", "Anne"}

print("friendsSet", friendsSet)
friendsSet.add("Smith")
friendsSet.add("Smith")
print("friendsSet", friendsSet)
friendsSet.remove("Smith")
print("friendsSet", friendsSet)
