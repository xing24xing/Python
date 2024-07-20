my_array = [64,34,25,5,22,11,90,12]
n = len(my_array)
for i in range(n-1):
    min_idx = i
    for j in range(i+1,n):
        if my_array[j] < my_array[min_idx]:
            min_idx = j
    min_value = my_array.pop(min_idx)
    my_array.insert(i,min_value)
print("Sorted Array : ",my_array)

# 2.
print("Selection Sort Shifting Problem")

my_array =  [64,34,25,5,22,11,90,12]
n = len(my_array)
for i in range(n-1):
    min_idx = i
    for j in range(i+1,n):
        if my_array[j] < my_array[min_idx]:
            min_idx = j
    my_array[i],my_array[min_idx] = my_array[min_idx],my_array[i]
print("Sorted Array : ", my_array)