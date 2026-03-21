# Day 1: Palindrome.py
def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return rev
num = int(input("Enter the number: "))
if num == reverse_number(num):
    print("Palindrome")
else:
    print("Not Palindrome")
