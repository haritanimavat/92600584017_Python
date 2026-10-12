# 10. Extract specific information from a text using regular expressions


import re

text = "Name: Harita, Age: 20, Phone: 9876111110"

name = re.search(r"Name: (\w+)", text).group(1)
age = re.search(r"Age: (\d+)", text).group(1)
phone = re.search(r"Phone: (\d+)", text).group(1)

print("Name:", name)
print("Age:", age)
print("Phone:", phone)
