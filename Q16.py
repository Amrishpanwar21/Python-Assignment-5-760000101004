# Write mode
file = open("demo.txt", "w")
file.write("Hello")
file.close()

# Append mode
file = open("demo.txt", "a")
file.write("\nWelcome")
file.close()

# Read file
file = open("demo.txt", "r")
print(file.read())
file.close()