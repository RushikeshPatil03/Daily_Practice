#day3_strong_number.py
def is_strong(n):
    if n==0:
        return False
    num=n
    s=0
    while num>0:
        fact=1
        digit=num%10
        for i in range(1,digit+1):
            fact*=i
        s+=fact
        num//=10
    return s==n
n = int(input("Enter the number: "))
if is_strong(n):
    print(f"{n} is a Strong Number")
else:
    print(f"{n} is Not a Strong Number")
