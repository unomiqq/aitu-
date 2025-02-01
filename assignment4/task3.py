def name_search(names, target_name):
    for i, name in enumerate(names):
        if name.lower() == target_name.lower():
            return i
    return -1

names = ["John", "Alice", "Bob", "Eve", "Mike"]
target_name = "Alice"
index = name_search(names, target_name)

if index != -1:
    print(f"Name '{target_name}' found at index {index}")
else:
    print(f"Name '{target_name}' not found in the list")