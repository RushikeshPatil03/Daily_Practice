# Day 4: GCD using Euclidean Algorithm

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


x, y = map(int, input("Enter two numbers: ").split())

print(f"GCD of {x}, {y} is: {gcd(x, y)}")
