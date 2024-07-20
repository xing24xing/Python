my_array = [64, 34, 25, 5, 22, 11, 90, 12]
n = len(my_array)
for i in range(n-1):
    insert_idx = i
    current_val = my_array.pop(i)
    for j in range(i-1,-1,-1):
        if my_array[j] > current_val:
            insert_idx = j
    my_array.insert(insert_idx,current_val)
print("sorted array : ",my_array)

print("Improved Solution")
my_array = [23,45,122,34,15,78]
n = len(my_array)
for i in range(1,n):
    insert_idx = i
    current_val = my_array[i]
    for j in range(i-1,-1,-1):
        if my_array[j]>current_val:
            my_array[j+1] = my_array[j]
            insert_idx = j
        else:
            break
    my_array[insert_idx] = current_val
print("Sorted array : ",my_array)

