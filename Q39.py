file1 = open("data.txt", "r")

data = file1.read()

file1.close()

reverse = data[::-1]

file2 = open("reverse.txt", "w")

file2.write(reverse)

file2.close()

print("Reverse data saved successfully")