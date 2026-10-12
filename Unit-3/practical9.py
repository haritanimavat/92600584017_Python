# 9. Use match(), search() and findall()


import re

text = "Hello 123 World 456"

print(re.match("Hello", text))
print(re.search(r"\d+", text).group())
print(re.findall(r"\d+", text))
