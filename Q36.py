file = open("data.txt", "r")

data = file.read()

words = data.split()

longest = ""

for word in words:
    word = word.strip(".,!?;:\"'()")
    if len(word) > len(longest):
        longest = word

print("Longest word =", longest)

file.close()