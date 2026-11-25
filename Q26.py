file = open("demo.txt", "a+")

file.write("\nNew data added")

file.seek(0)

print(file.read())

file.close()