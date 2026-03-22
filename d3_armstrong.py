#day3_armstrong.py
import math
n=int(input("Enter the number : "))
def is_armstrong(n):
    num=n
    digits_count=int(math.log10(n)+1)
    sum=0
    while num>0:
        digit=num%10
        sum+=digit**digits_count
        num//=10
    if n==sum:
        print(f"{n} is a Armstrong Number")
    else:
        print(f"{n} is Not a Armstrong Number")
is_armstrong(n)
