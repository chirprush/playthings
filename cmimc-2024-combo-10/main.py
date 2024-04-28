from math import factorial, e, comb, gcd

def derangements(n):
    s = 0

    for i in range(0, n+1):
        s += (-1) ** i * factorial(n) // factorial(i)

    return s

num = 0

for i in range(0, 101):
    num += comb(100, i) * derangements(100 - i) * i ** 5

G = gcd(num, factorial(100))
print(num // G, "/", factorial(100) // G)
