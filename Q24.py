file = open("demo.txt", "r+")

print("Old data:")
print(file.read())

file.seek(0)

file.write("Hello")

file.close()