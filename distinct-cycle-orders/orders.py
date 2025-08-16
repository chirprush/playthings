from sage.all import SymmetricGroup
from sympy import totient

n = 6
orders = {}

for p in list(SymmetricGroup(n)):
    o = p.order()

    if o in orders:
        orders[o] += 1
    else:
        orders[o] = 1

for o in sorted(orders.keys()):
    t = totient(o)
    assert orders[o] % t == 0

    print(f"{o}, {orders[o]}, {orders[o] // t}")
