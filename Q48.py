import os

filename = "data.txt"

if os.path.exists(filename):
    print("File exists")

    size = os.path.getsize(filename)

    print("File size =", size, "bytes")
else:
    print("File does not exist")