First_no = int(input("Enter First Number\n"))
Second_no = int(input("Enter Second Nuumber\n"))
Third_no = int(input("Enter Third Number\n"))
if First_no > Second_no and First_no > Third_no:
    print(First_no," Number Is Maximum")
elif Second_no > First_no and Second_no > Third_no:
    print(Second_no," Number Is Maximum")
else:
    print(Third_no," Number Is Maximum")


if First_no < Second_no and First_no < Third_no:
    print(First_no," Number Is Minimum")
elif Second_no < First_no and Second_no < Third_no:
    print(Second_no," Number Is Minimum")
else:
    print(Third_no," Number Is Minimum")
