text = input("Enter your text: ")

file = open("user.txt", "w")

file.write(text)

file.close()

print("Text saved successfully")