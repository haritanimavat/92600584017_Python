# 6. File and directory operations using os and sys


import os
import sys

print("Current directory:", os.getcwd())

os.mkdir("test")
print("Directory created")

print("Python version:", sys.version)
