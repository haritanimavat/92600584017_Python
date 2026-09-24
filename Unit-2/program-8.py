# Write a program to illustrate variable scope
# using local, global and nonlocal variables.

x=10

def outer():
    y=20
    def inner():
        nonlocal y
        y=30
        print("Nonlocal variable:",y)
    inner()

def display():
    x=50
    print("Local variable:",x)
display()

print("Global variable:",x)
outer()
