# Write a program to demonstrate the use of break, continue and pass statements.

print("using break:")
for i in range(1,6):
    if i==4:
        break
    print(i)

print("________________________")

print("using continue:")
for i in range(1,6):
    if i==3:
        continue
    print(i)

print("________________________")

print("using pass:")
for i in range(1,6):
    if i==3:
        pass
    print(i)
