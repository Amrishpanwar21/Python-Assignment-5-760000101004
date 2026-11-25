file = open("data.txt", "r")

data = file.read()

word = input("Enter word to search: ")

if word.lower() in data.lower().split():
    print("Word exists in file")
else:
    print("Word does not exist")

file.close()