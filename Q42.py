import os

filename = "data.txt"

if os.path.exists(filename):
    print("File name:", os.path.basename(filename))
    print("File size:", os.path.getsize(filename), "bytes")
    print("File path:", os.path.abspath(filename))
else:
    print("File does not exist")