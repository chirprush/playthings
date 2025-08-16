from sympy import divisors
from itertools import product

p = 2

# Kinda slow to compute but it should be fine
def conv(f, g):
    assert len(f) == len(g)

    n = len(f)

    h = [0] * n

    for k in range(1, n + 1):
        for d in divisors(k):
            h[k - 1] += f[d - 1] * g[k // d - 1] % p

        h[k - 1] %= p

    return h

def power(g, n):
    res = [1 if i == 0 else 0 for i in range(len(g))]

    while n >= 1:
        if n % 2 == 0:
            g = conv(g, g)
            n //= 2
        else:
            res = conv(res, g)
            n -= 1

    return res

def order(g, verbose=False):
    n = len(g)

    ident = [1 if i == 0 else 0 for i in range(n)]
    res = g

    i = 1

    while True:
        if verbose:
            print(f"g^{i}: {res}")

        if res == ident:
            return i

        res = conv(res, g)

        i += 1

def order_table(n):
    orders = {}

    for g in product(range(p), repeat=n):
        if g[0] == 0:
            continue

        g = list(g)
        o = order(g)

        if o in orders:
            orders[o] += 1
        else:
            orders[o] = 1

    return orders

def oat(values, n):
    g = [0] * n

    for i in values:
        g[i - 1] = 1

    return g

print(order(oat([1, 2], 16), True))
# print(order_table(16))
