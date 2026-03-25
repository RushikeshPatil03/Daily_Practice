def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
def left_rotate_k(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    k = k % n 
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)
    return arr
arr = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter k: "))
print(left_rotate_k(arr, k))
