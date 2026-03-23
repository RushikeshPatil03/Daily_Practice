#day4_gcd_basic.py
a,b=map(int,input().split(' '))
def basic_gcd(m,n):
    gcd=1
    for i in range(1,min(m,n)):
        if m%i==0 and n%i==0:
            gcd=i
    return gcd
print(f'GCD of {a},{b} is : {basic_gcd(a,b)}')
