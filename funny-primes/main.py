from sympy.ntheory import isprime

for power in range(1, 20):
    for d in range(1, 10):
        n = d * 10 ** power - 1
        if isprime(n):
            print(n)
        n = d * 10 ** power + 1
        if isprime(n):
            print(n)
