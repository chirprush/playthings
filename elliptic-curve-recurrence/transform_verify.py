from sympy import simplify, expand, sqrt
from sympy.abc import x, y

def t(p):
    x, y = p
    return (y - 1) ** 2 / x **2 - x, (y - 1) - (y - 1) ** 3 / x ** 3 - 1

def phi(p):
    x, y = p
    return x, (y - 1) ** 2 / x ** 2 - x

def iphi(p):
    x, y = p
    return x, x * sqrt(x + y) + 1

s = (1, -1)
s = phi(t(iphi(s)))
print(s)

s = phi(t(iphi(s)))
print(s)

# a_n is the sequence 1 -1 5 19/25 ...
# And this is indeed phi(E(1, 1) + n * E(0, 1))
#                  = phi((wp(u_0 + n * w), wp'(u_0 + n * w)))
# Yay!
