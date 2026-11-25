file1 = open("data.txt", "r")

data = file1.read()

file1.close()

file2 = open("upper.txt", "w")

file2.write(data.upper())

file2.close()

print("Data converted into uppercase")