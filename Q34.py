file = open("data.txt", "r")

data = file.read()

word = input("Enter word: ")

words = data.split()

count = 0

for w in words:
    if w.lower() == word.lower():
        count = count + 1

print("Word occurrences =", count)

file.close()