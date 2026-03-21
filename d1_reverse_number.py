# Day 1: Reverse a Number
num = int(input("Enter the number: "))
n = num
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10
print(f"Reverse of {num}: {rev}")
