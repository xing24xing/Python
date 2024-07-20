my_array = [64,34,25,12,22,11,90,5]
n = len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j],my_array[j+1] = my_array [j+1],my_array[j]
print("Sorted Array : ",my_array)

print("Bubble Sort Improvement")
my_array = [7,3,1,2,4,9,12,11,13,14,15,16]
n = len(my_array)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j],my_array[j+1]= my_array[j+1],my_array[j]
            swapped = True
            # print("This is not Already Sorted")
    if not swapped:
        # print("This Is already Sorted")
        break
print("Sorted Array :",my_array)