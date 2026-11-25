file = open("data.txt", "r")

ch = input("Enter starting character: ")

for line in file:
    if line.startswith(ch):
        print(line, end="")

file.close()