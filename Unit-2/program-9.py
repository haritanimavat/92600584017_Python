# Write a program to demonstrate iterators and iterables in Python.

list1=["Apple","Banana","Mango"]

print("Iterable:")
for x in list1:
    print(x)

print("________________________")

print("Iterator:")
it=iter(list1)

print(next(it))
print(next(it))
print(next(it))
