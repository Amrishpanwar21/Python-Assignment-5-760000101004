import os

old_name = "data.txt"
new_name = "updated.txt"

if os.path.exists(old_name):
    os.rename(old_name, new_name)

    file = open(new_name, "r")

    print(file.read())

    file.close()

else:
    print("File does not exist")