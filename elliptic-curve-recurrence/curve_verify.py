from sympy import Poly, rem, expand, simplify
from sympy.abc import x, y, u, v, a, b

def f1(x, y):
    return (y - 1) ** 2 / x ** 2 - x, (y - 1) - (y - 1) ** 3 / x ** 3 - 1

def f2(x, y):
    return y ** 2 - x, x * y - y ** 3 - 1

curve = y ** 2 - x ** 3 + x - 1

# curve_iphi = expand((u * v + 1) ** 2 - u ** 3 + u - 1)
acurve = expand(u ** 3 * curve.subs({x: phi1(u, v)[0], y: phi1(u, v)[1]}))
print(acurve)
print(rem(acurve, curve.subs({x: u, y: v})))


# curve_iphi(u, v) is such that curve_iphi(g(x, y)) = curve(x, y), where g(x, y) = (x, (y - 1) / x)
# curve(f(x, y)) mod curve(x, y) = 0, where f(x, y) = ((y - 1) ** 2 / x ** 2 - x, (y - 1) - (y - 1) ** 3 / x ** 3 - 1)
# curve(phi(g(x, y))) mod curve(x, y) as phi(g(x, y)) = f(x, y), where phi(u, v) = v ** 2 - u, uv - v ** 3 - 1
