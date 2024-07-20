num = int(input("Enter Any Number\n"))
n = num
while(n > 0):
    r = int(n % 10)
    print(r)
    n = int(n / 10)