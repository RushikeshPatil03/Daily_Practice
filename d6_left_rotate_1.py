#day6_left_rotate_1.py
def left_rotate(arr):
    first=arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[-1]=first
    return arr
arr=list(map(int,input("Enter the array elements : ").split(' ')))   
print(left_rotate(arr))
