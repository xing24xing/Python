first_no = int(input("Enter First Number\n"))
second_no = int(input("Enter Second Number\n"))
first_no = first_no ^ second_no
second_no = first_no ^ second_no
first_no = first_no ^ second_no

print("1.)Swapping Two Number By Using Bit Method:-", first_no, " ", second_no)

first_no1 = int(input("Enter First Number\n"))
second_no1 = int(input("Enter Second Number\n"))
temp = first_no1
first_no1 = second_no1
second_no1 = temp

print("2.)Swapping Two Number By Using Third Variable:- ", first_no1, " ", second_no1)

first_no2 = int(input("Enter First Number\n"))
second_no2 = int(input("Enter Second Number\n"))
first_no2 = first_no2 + second_no2
second_no2 = first_no2 - second_no2
first_no2 = first_no2 - second_no2

print("3.)Swapping Two Number Without using Third Variable:- ", first_no2, " ", second_no2)


