# Day 3: Perfect Number
def is_perfect(n):
    if n <= 1:
        return False
    divisor_sum = 1 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:
                divisor_sum += n // i
    return divisor_sum == n
n = int(input("Enter the number: "))
if is_perfect(num):
    print(f"{num} is a Perfect Number")
else:
    print(f"{num} is Not a Perfect Number")
