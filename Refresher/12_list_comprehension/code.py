numbers = [1, 2, 3]

doubledLoop = []
for num in numbers:
    doubledLoop.append(num * 2)

doubled = [num * 2 for num in numbers]

print("doubledLoop", doubledLoop)
print("doubled", doubled)

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]

starts_s_loop = []
for friend in friends:
    if friend.startswith("S"):
        starts_s_loop.append(friend)

starts_s = [friend for friend in friends if friend.startswith("S")]

print("starts_s_loop", starts_s_loop)
print("starts_s", starts_s)