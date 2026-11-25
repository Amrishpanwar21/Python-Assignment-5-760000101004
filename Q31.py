file = open("data.txt", "r")

data = file.read()

count = 0

for ch in data:
    if ch in "aeiouAEIOU":
        count = count + 1

print("Total vowels =", count)

file.close()