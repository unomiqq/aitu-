def find_max_value(arr):
    if not arr:
        return None, -1

    max_value = arr[0]
    max_index = 0

    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i
    return max_value, max_index

array = [5, 12, 9, 21, 3]
print(find_max_value(array))

max_value, max_index = find_max_value(array)

if max_value is not None:
    print(f"Maximum value is {max_value} at index {max_index} ")
else:
    print("Array is empty")