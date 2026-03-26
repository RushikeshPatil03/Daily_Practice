# Day 7: Binary Search (Recursive)
def binary_search_recursive(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, low, mid - 1, target)
    else:
        return binary_search_recursive(arr, mid + 1, high, target)
arr = list(map(int, input("Enter sorted elements: ").split()))
target = int(input("Enter target: "))
result = binary_search_recursive(arr, 0, len(arr) - 1, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print("Target not found")
