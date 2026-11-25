file = open("data.txt", "r")

data = file.read()

count = len(data)

print("Total characters =", count)

file.close()