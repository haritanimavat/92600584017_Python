#Write a program to demonstrate conditional statements using if if-else and if-elif-else.

n=int(input("enter value:"))

if n%2==0:
    print("Even")
else:
    print("Odd")

print("____________________________________")

n1=int(input("enter value for n1:"))
n2=int(input("enter value for n2:"))
n3=int(input("enter value for n3:"))

if n1>n2 and n1>n3:
    print("n1 is a maximum")
elif n2>n1 and n2>n3:
    print("n2 is a maximum")
else:
    print("n3 is a maximum")
