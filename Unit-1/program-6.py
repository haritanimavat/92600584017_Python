#write a program to illustrate the use of tuples and sets with basic operations.

#tuples
tpl=(5,10,15,20,25,30,35)
print(tpl)
print("first element:",tpl[0])
print("middle elements(2:5):",tpl[2:5])
print("middle element(-4):",tpl[-4])
print("last element(-1):",tpl[-1])

set1={2,4,6,8,3}
set2={1,3,5,7}

print("set1 is :",set1)
print("set2 is :",set2)

print("joint:",set1|set2)
print("simillar",set1&set2)
print("difference",set1-set2)

set1.add(12)
print("after add(set1):",set1)

set2.remove(7)
print("after remove(set2)",set2)
