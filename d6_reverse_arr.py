#Day 6 Reverse the given array without using extra space
def reverse_arr(arr):
    left=0
    right=len(arr)-1
    while left < right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr
arr=list(map(int,input("Enter the array elements : ").split(' ')))
print(reverse_arr(arr))
