#using while loop
print("Print Number Using while Loop")
i = 1
while(i <= 10):
    print(i)
    i = i + 1
# print("\n")
print("Print Number Using For Loop")

for j in range(0,11,2):
    if(j == 2):
        continue
    if(j == 8):
        break
    print(j," ")

# a = 10
# b = 10
# c = 10
# if(a == b == c):
#     print("Hello")
# else:
#     print("Bye Bye")
