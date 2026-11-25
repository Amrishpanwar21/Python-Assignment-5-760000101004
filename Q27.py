file = open("data.txt", "r")

print("Position:", file.tell())

file.read(5)

print("New position:", file.tell())

file.close()