import os

filename = "data.txt"

if os.path.exists(filename):
    print("File exists")
else:
    print("File does not exist")