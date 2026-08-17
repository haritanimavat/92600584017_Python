#write a program to demonstrate recursion using factorial or fibonanci series.

#fibonancci

def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

n=int(input("enter value for fibonanci series:"))
print("fibonanci series is :")
for i in range(n):
    print(fib(i),end=" ")
print("\n")


#factorial

n=int(input("enter value for factorial:"))
print("factorail is :")
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(n))


    
    
