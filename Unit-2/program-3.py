#Write a program to generate a multiplication table using a for loop.

n=int(input("enter value:"))

for i in range(1,11):
    mul=n*i
    print(n,"*",i,"=",mul)
