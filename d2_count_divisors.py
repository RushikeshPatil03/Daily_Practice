# Day 2: Count Divisors
def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count
num = int(input("Enter the number: "))
print(f"Number of divisors of {num}: {count_divisors(num)}")
