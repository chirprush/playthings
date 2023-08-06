# from sympy import isprime
from math import sqrt, floor

def D(b):
    return sum(
        (i + 1) * b ** i
        for i in range(b - 1)
    )

def isprime(d):
    if d % 2 == 0:
        return False, 2
    for i in range(3, floor(sqrt(d)), 2):
        if d % i == 0:
            return False, i
    return True, d

if __name__ == "__main__":
    for b in range(2, 1000):
        d = D(b)
        prime, prime_divisor = isprime(d)
        if prime:
            print(f"D({b}) = {d} is prime")
        else:
            print(f"D({b}) = {d} is not prime with smallest prime divisor {prime_divisor}")
