import os

# Create and write file
file = open("test.txt", "w")

file.write("Hello Python Programming")

file.close()

# Read the file
file = open("test.txt", "r")

print("File contents:")
print(file.read())

file.close()

# Delete the file
os.remove("test.txt")

print("File closed and deleted successfully")