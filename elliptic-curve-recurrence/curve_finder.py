from sympy import Poly, rem, QQ, symbols, Matrix, Rational, expand
from sympy.abc import x, y

deg = 3
counter = 0

a = [symbols(f"a{i}") for i in range(10)]


f_total = 0
ft_total = 0

xp = y
yp = x * y - x ** 3 - 1

for i in range(deg + 1):
    for j in range(deg - i + 1):
        f_total += symbols(f"a{counter}") * x ** i * y ** j
        ft_total += symbols(f"a{counter}") * xp ** i * yp ** j
        counter += 1

f = Poly(f_total, x, y)
ft = Poly(expand(ft_total), x, y)

print(f)
print(ft)
# a9*x**3 + a8*x**2*y + a7*x**2 + a6*x*y**2 + a5*x*y + a4*x + a3*y**3 + a2*y**2 + a1*y + a0

co = rem(ft, f).coeffs()
print(co)

# Hmmm even then a0 = 0 bro what
print([i.subs({a[0]: 1, a[9]: 1, a[8]: 0, a[6]: 0, a[7]: 0, a[2]: 1}) for i in co])
