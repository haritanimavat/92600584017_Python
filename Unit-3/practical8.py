# 8. Basic regular expression pattern matching


import re

text = "My number is 12345"

if re.search(r"\d+", text):
    print("Number found")
else:
    print("Number not found")
