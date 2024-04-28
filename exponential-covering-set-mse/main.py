def f(n, p):
    return (pow(2, n, p) + 1518781) % p

primes = set()

for n in range(1, 1000001):
    p = 2
    while f(n, p) != 0:
        p += 1
    primes.add(p)

print(primes)
# print(set(primes))
