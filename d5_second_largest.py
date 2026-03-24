# Day 5: Second Largest Element (Optimal)
def find_second_largest(arr):
    if len(arr) < 2:
        return None
    largest = second = float('-inf')
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num
    return second if second != float('-inf') else None


arr = list(map(int, input("Enter elements: ").split()))

result = find_second_largest(arr)

if result is None:
    print("No second largest element")
else:
    print(f"Second largest element: {result}")
