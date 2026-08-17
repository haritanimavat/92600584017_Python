#Write a program to perform arithmetic relational and logical operations using Python operators.

num1=int(input("enter value :"))
num2=int(input("enter value :"))

print("-------------Arithmetic Operator-------------")

print("Addition Is :",num1+num2)
print("Substraction Is :",num1-num2)
print("Multiplication Is:",num1*num2)
print("Division Is :",num1/num2)
print("Floor Is :",num1//num2)
print("Power Is :",num1**num2)
print("Moduolus Is :",num1%num2)

print("-------------Relational Operator-------------")

print("Num1 is ",num1,":: Num2 Is :: ",num2,"-->(Equal)-->",num1==num2)
print("Num1 is ",num1,":: Num2 Is :: ",num2,"-->(Not Equal)-->",num1!=num2)
print("Num1 is ",num1,":: Num2 Is :: ",num2,"-->(Greater Than)-->",num1>num2)
print("Num1 is ",num1,":: Num2 Is :: ",num2,"-->(Greater Than Or Equal)-->",num1>=num2)
print("Num1 is ",num1,":: Num2 Is :: ",num2,"-->(Less Than)-->",num1<num2)
print("Num1 is ",num1,":: Num2 Is :: ",num2,"-->(Less Than Or Equal)-->",num1<=num2)  

print("-------------Logical Operator-------------")

print("Num1 is ",num1,":: Num2 Is :: ",num2,"-->(And)-->",num1>num2 and num1>=num2)
print("Num1 is ",num1,":: Num2 Is :: ",num2,"-->(Or)-->",num1<num2 or num1<=num2)
print("Num1 is ",num1,":: Num2 Is :: ",num2,"-->(Not)-->",not(num1>num2))


