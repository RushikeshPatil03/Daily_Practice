# Day 5: Check if Array is Sorted
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

arr = list(map(int, input("Enter elements: ").split()))

if not arr:
    print("Array is empty")
else:
    if is_sorted(arr):
        print("Array is sorted")
    else:
        print("Array is not sorted")
