# Write a program to demonstrate list dictionary and set comprehensions.

nm=input("enter value:")
ag=int(input("enter value:"))

list1=[{"my name is {} and my age is {}".format(nm,ag)}]
print(list1)

n=int(input("enter value:"))
m=int(input("enter value:"))
squ=[x*x for x in range(n,m+1)]
print(squ)
