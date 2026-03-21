#day2_prime_check.py
def prime_check(n):
    if n<=1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        else:
            return True
num=int(input('Enter the number : '))
if prime_check(num):
    print('Prime Number')
else:
    print('Not Prime Number')
