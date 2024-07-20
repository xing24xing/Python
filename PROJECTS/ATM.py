i = 1
a = 10000
pin = 1111
otp = 000
phone = 9165789955
newotp = 333
print("Welcome To ABC Bank")
pin1 = int(input("Please Enter Your Pin : "))

if(pin1==pin):
  while i < 2:
    if pin == pin1:
        print("1. Balance Enquiry ")
        print("2. Cash Withdrawal")
        print("3. Deposit")
        print("4. Change Pin")
        print("5. Check Mobile Number")
        print("6. Change Mobile Number")
        print("7. Exit")
        op = int(input())
        if op == 1:
            print("Your Current Balance is : ",a)
        elif op == 2:

            b = int(input("Enter The Amount : "))
            if a >= b and (a > 500 and b > 500):
                a = a - b
                print("Transaction Successfully Done")
            elif a < b and (a < 500 and b < 500):
                print("You Have Insufficient Balance")
            else:
                print("You Have Insufficient Balance")
        elif op == 3:
            b = int(input("Enter The Amount : "))
            a += b
            print("Transaction Successfully Done")
        elif op == 4:
            n = int(input("Enter Old Pin"))
            if pin == n:
                pin1 = int(input("Enter New Pin"))
                pin2 = int(input("Confirm New Pin"))
                if pin1 == pin2:
                    pin == pin2 == pin1
                    print("Your Pin Has Been Successfully Changed")
                    print("Your Pin Is : ",pin2)
                elif pin1 != pin2:
                    print("Your Pin Does Not Match")
                else:
                    print(IOError)
        elif op == 5:
            print("Your Mobile Number : ",phone)
        elif op == 6:
            z = int(input("Enter Your Old Mobile Number : "))
            if phone == z:
                print("OTP has been sent to 91******55")
                l = int(input("Please enter the OTP Sent to 91******55: "))
                if otp == l:
                    x = int(input("Enter Your New Mobile Number : "))
                    y = int(input("Confirm Your New Mobile Number : "))
                    if x == y:
                        print("OTP has Been Sent To The New Number..")
                        k = int(input("Enter The OTP : "))
                        if newotp == k:
                            phone == x == y
                            phone = x
                            print("Your Phone Has Been Successfully Changed")
                            print("Your Mobile Number Is : ",y)
                    elif x != y:
                       print("Your Mobile Number Does not Match")
                    else:
                        print(IOError)
        elif op == 7:
            i += 1
            print("Please Visit Again...")
        else:
            print("Exit")
else:
    print("It is An Invalid Pin")
