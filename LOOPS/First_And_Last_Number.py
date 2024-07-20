num = int(input("Enter Any Number\n"))
n = num
last = num % 10
while(n > 0):
    first = int(n % 10)
    n = int(n / 10)
print("First Number : ", first)
print("Last Number : ", last)