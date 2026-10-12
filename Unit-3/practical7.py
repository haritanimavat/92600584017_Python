# 7. Copy, move and delete files using shutil


import shutil
import os

with open("a.txt", "w") as f:
    f.write("Hello")

shutil.copy("a.txt", "b.txt")
print("File copied")

shutil.move("b.txt", "c.txt")
print("File moved")

os.remove("c.txt")
print("File deleted")
