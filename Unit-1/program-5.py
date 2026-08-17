# write a program to create and manipulate lists using indexing slicing and list comprehension

#indexing
values=[5,10,15,20,25]
print(values)
print("value 1: ",values[1])
print("value 2: ",values[3])
print("value -1 :",values[-1])

#slicing
print("value 1:4 = ",values[1:4])
print("value -2:...= ",values[-2:])

#list comprehension
sq=[x*x for x in values]
print("squares :",sq)

