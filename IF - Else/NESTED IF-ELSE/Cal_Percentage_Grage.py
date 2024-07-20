name = input("Enter Your Name\n")
std = int(input("Enter The Class\n"))
english = int(input("Enter The English Marks\n"))
hindi = int(input("Enter The Hindi Marks\n"))
marathi = int(input("Enter The Marathi Marks\n"))
Evs = int(input("Enter The EVS Marks\n"))
GK = int(input("Enter Your GK Marks\n"))
play_do_learn = int(input("Enter The Play Do Learn Marks\n"))
maths = int(input("Enter The Maths Marks\n"))
computer = int(input("Enter The Computer Marks\n"))
total = english + hindi + marathi + Evs + GK + play_do_learn + maths + computer
percentage = (total * 100)/800
print("Name :",name)
print("Class : ",std)
print("English : ",english)
print("Hindi : ",hindi)
print("Marathi : ",marathi)
print("EVS : ",Evs)
print("GK : ",GK)
print("Play Do Learn : ",play_do_learn)
print("Maths : ",maths)
print("Computer : ",computer)
print("Percentage : ",percentage)
if percentage<=99 and percentage>90:
    print("Grade = A+")
elif percentage <= 90 and percentage >80:
    print("Grade = A")
elif percentage <= 80 and percentage >70:
    print("Grade = B+")
elif percentage <= 70 and percentage > 60:
    print("Grade = B")
elif percentage <= 60 and percentage >50:
    print("Grade = C+")
elif percentage <= 50 and percentage > 40:
    print("Grade = D+")
else:
    print("Fail")
print("Minimum Marks",min(english,hindi,marathi,Evs,GK,play_do_learn,maths,computer))

print("Maximum Marks",max(english,hindi,marathi,Evs,GK,play_do_learn,maths,computer))