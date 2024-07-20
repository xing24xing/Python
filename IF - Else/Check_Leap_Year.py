num = int(input("Enter Any Number\n"))
if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
    print(num," Is A Leap Year")
else:
    print(num," Is A Simple Year")