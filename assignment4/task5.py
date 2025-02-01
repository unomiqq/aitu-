def find_closer(arr, target):
    closest_index = 0
    closest_diff = abs(arr[0] - target)

    for i in range(1, len(arr)):
        diff = abs(arr[i] - target)
        if diff < closest_diff:
            closest_diff = diff
            closest_index = i
    return arr[closest_index], closest_index

array = [1, 3, 7, 9, 14]
target = 8

value, index = find_closer(array, target)
print(f"Closest value to {target} is {value} at index {index}")