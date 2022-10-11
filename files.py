import os
from os import path
from pathlib import Path

print("FILE MAIN.py")
file = open("main.py", "r")
print(file.read())
file.close()

# print("FILE VARIABLES2.py")
# with open("variables2.py", "r") as file:
#     #открытие файла
#     for line in file:
#         print(line)
#     #закрыте файла
#
# print("end ")

cur_path = os.getcwd()
files_dir = Path(cur_path) / "files"
print(files_dir)
try:
    files_dir.mkdir()
except FileExistsError:
    pass

file_path = files_dir / "file.txt"
with file_path.open('a+') as file:
    file.write("123")
    file.seek(0)
    print(file.read())

try:
    os.remove("file.txt")
except FileNotFoundError:
    pass

print(Path("file.txt").exists())


print(file_path)
print(path.basename(file_path))
print(path.dirname(file_path))
print(path.splitext("files.txt"))

print(path.abspath(path.join("..", "testdir")))


TEST = os.environ.get(
    "TEST",
    "default variable for environment variable"
)
print("test: ", TEST)
