file1 = open("data.txt", "r")

data = file1.read()

file1.close()

file2 = open("copy.txt", "w")

file2.write(data)

file2.close()

print("File copied successfully")