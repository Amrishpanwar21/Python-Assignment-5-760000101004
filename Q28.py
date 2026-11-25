file = open("data.txt", "r")

file.seek(6)

print(file.read())

file.close()