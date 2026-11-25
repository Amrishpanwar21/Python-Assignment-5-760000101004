file = open("data.txt", "r")

word = input("Enter word to search: ")

for line in file:
    if word.lower() in line.lower():
        print(line, end="")

file.close()