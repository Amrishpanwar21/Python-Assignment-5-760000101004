file = open("data.txt", "r")

print("Before closing:", file.closed)

file.close()

print("After closing:", file.closed)