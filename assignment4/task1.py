#Kovalenko Nikita cs-2434
#Task 1: Searching for a Specific Value in an Integer Array

def linear_search(arr, target) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = list(map(int, input("Enter the array: ").split(", ")))
target = int(input("Enter the target value: "))
print(linear_search(arr, target))