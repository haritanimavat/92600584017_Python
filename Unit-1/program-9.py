#write a program to define and use user-defined functions with different types of arguments.

def simple():
    print("have a good day...!")
simple()

def add(a,b):
    print("addition is :",a+b)
add(10,20)

def fix(uni="MU"):
    print("university is :",uni)
fix()    

def msg():
    return "nice to meet you...!"
res=msg()
print(res)
