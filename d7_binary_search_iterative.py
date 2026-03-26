# Day 7: Binary Search (Iterative)
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
arr = list(map(int, input("Enter sorted elements: ").split()))
target = int(input("Enter target: "))
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print("Target not found")
