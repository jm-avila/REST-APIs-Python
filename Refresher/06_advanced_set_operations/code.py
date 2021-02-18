art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

# difference takes one set and removes the items found at passed set.
onlyArt = art.difference(science)
onlyScience = science.difference(art)

print("only Art", onlyArt)
print("only Science", onlyScience)
print()

# intersection takes one set and removes the items not found at passed set.
both = art.intersection(science)

print("take both", both)
