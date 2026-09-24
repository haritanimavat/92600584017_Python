# Write a program to generate a sequence of numbers
# using generator functions and yield keyword.

def numbers(n):
    for i in range(1,n+1):
        yield i

n=int(input("Enter value: "))

for x in numbers(n):
    print(x)
