# Suppose l_1, l_2, ..., l_k is a partition of n.
# How many distinct values may lcm(l_1, l_2, ..., l_k) take on?

from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

lcms = set()

def add(running, n):
    if n == 0:
        lcms.add(running)

    for i in range(1, n + 1):
        add(lcm(running, i), n - i)

print("n, f(n)")
for i in range(2, 50):
    add(1, i)

    print(f"{i} {len(lcms)}")

# Using OEIS yields: https://oeis.org/A009490
# which is exactly what we wanted

# This could be useful for Project Euler #483
