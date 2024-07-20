print("1 . Printing Fibonacci Series Using Loop")
first = 0
second = 1
print(first)
print(second)
for fibo in range(10):
    third = first + second
    first = second
    second = third
    print(third)
print("\n")
# Implementation using recursion
print("2 . Printing Fibonacci Series Using ReCursive Function")
print(0)
print(1)
count = 2
def fibo(first,second):
    global count
    if count <= 10:
        newfibo = first + second
        first = second
        second = newfibo
        print(newfibo)
        count+=1
        fibo(first,second)
    else:
        return
fibo(1,0)
print("\n")
# 3 implementation using recursion
print("3 . Printing Fibonacci Series Using Recursive Function")
def F(n):
    if n <= 1:
        return n
    else:
       return F(n-1)+F(n-2)
print(F(10))


