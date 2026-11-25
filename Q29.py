file = open("data.txt", "r")

file.seek(6)

data = file.read()

print(data)

file.close()