file = open("data.txt", "r")

line1 = file.readline()
line2 = file.readline()
line3 = file.readline()

print(line1, end="")
print(line2, end="")
print(line3, end="")

file.close()