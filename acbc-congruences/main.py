from math import gcd

n = 6
c = 3

assert(gcd(n, c) != 1)

first_cond = []
second_cond = []

for a in range(n):
    for b in range(a + 1, n):
        if (a * c % n) == (b * c % n):
            first_cond.append((a, b))
            
            if a % n == b % n:
                second_cond.append((a, b))

print("Pairs: " + repr(first_cond))
print("Pairs fulfill: " + repr(second_cond))
