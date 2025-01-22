def buble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [20, 10, 33, 8, 12, 18, 52, 1]
print(arr)
print(buble_sort(arr))