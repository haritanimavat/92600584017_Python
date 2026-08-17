#write a program to create a dictionary and demonstrate dictionary methods and iteration.

#methods
dic={
    "name":"harita",
    "age":21,
    "university":"MU",
    "city":"rajkot"
    }
print("name:",dic["name"])
print("city:",dic["city"])

print("keys:",dic.keys())
print("values:",dic.values())
print("items:",dic.items())

dic["course"]="MCA"
print("after adding value:",dic)

dic["city"]="rjk"
print("after change the value:",dic)

#iteration
for key,value in dic.items():
    print(key,":",value)











