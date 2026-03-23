def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return (a * b) // gcd(a, b)


a, b = map(int, input("Enter two numbers: ").split())

print(f"LCM of {a}, {b} is: {lcm(a, b)}")
