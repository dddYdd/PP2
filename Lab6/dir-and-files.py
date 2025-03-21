#1
import os
path = "."
print("Directories:")
print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
print("Files:")
print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

#2
import os
path = "."
print("Exists:", os.access(path, os.F_OK))
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))

#3
import os
path = "example.txt"
if os.path.exists(path):
    print("Path exists")
    print("Filename:", os.path.basename(path))
    print("Directory:", os.path.dirname(path))
else:
    print("Path does not exist")

#4
file_path = "sample.txt"
with open(file_path, "r") as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))

#5
data = ["Python", "Java", "C++"]
with open("languages.txt", "w") as file:
    for item in data:
        file.write(item + "\n")

#6
import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as file:
        file.write(f"This is file {letter}.txt")

#7
with open("source.txt", "r") as src, open("destination.txt", "w") as dest:
    dest.write(src.read())

#8
import os
file_path = "delete_me.txt"
if os.path.exists(file_path) and os.access(file_path, os.W_OK):
    os.remove(file_path)
    print("File deleted")
else:
    print("File not accessible or doesn't exist")
