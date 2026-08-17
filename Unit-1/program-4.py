#write a program to demonstrate string operations including slicing formatting and built in string operations

#slicing

sen="Create What's Next...!"

print(sen)
print(sen[0:5])
print(sen[9:])
print(sen[5:9])

#formatting

un=input("Enter University Name :")
ct=input("Enter City Name :")

print("my university name is {} and city is {}".format(un,ct))
print(f"my university name is {un} and city is {ct}")

#buit-in string function

uni="Marwadi University"

print("lower:",uni.lower())
print("upper",uni.upper())
print("length",len(uni))
print("replace:",uni.replace("Marwadi","Atmiya"))
print("alphabatic:",uni.isalpha())
print("split:",uni.split())
print("count of a:",uni.count("a"))





