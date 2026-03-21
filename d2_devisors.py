#Day_2 Devisors.py
def devisors(n):
    s=[]
    l=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            s.append(i)
            if i!=n//i:
                l.append(n//i)
    print(f'Divisors of the {n} are : {sorted(s+l)}')
num=int(input('Enter the Number : '))
devisors(num)
