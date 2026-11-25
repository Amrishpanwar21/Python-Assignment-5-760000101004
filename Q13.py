file = open("lines.txt", "w")

lines = [
    "Hello Python\n",
    "Welcome to programming\n",
    "File handling is easy\n"
]

file.writelines(lines)

file.close()

print("Lines written successfully")