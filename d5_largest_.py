# Day 5: Largest Element in Array
arr = list(map(int, input("Enter elements: ").split()))
if not arr:
    print("Array is empty")
else:
    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    print(f"Largest element: {max_val}")
