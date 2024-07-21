from typing import Callable

from numpy import real, imag
from scipy.integrate import quad

from cmath import cos, sin
from math import pi, factorial

RtoC = Callable[[float], complex]
CtoC = Callable[[complex], complex]

class Contour:
    pass

class CircleContour(Contour):
    def __init__(self, r: float = 1) -> None:
        self.start = 0
        self.end = 2 * pi
        self.r = r

    # A simple parametric circle in the complex plane
    # t goes from 0 to 2pi
    def path(self, t: float) -> complex:
        return self.r * (cos(t) + 1j * sin(t))

    def path_prime(self, t: float) -> complex:
        return self.r * (1j * cos(t) - sin(t))

# A helper integration function that works with complex numbers
def integrate(f: RtoC, a: float, b: float) -> complex:
    real_part = quad(lambda t: real(f(t)), a, b, limit=100)[0]
    imag_part = quad(lambda t: imag(f(t)), a, b, limit=100)[0]
    
    return real_part + 1j * imag_part

# The definition of Cauchy's formula for derivatives (minus the factorial
# multiplication because that causes overflows too easily)
# We convert the contour integral to a Riemann integral by the definition
def F_n(f: CtoC, z: complex, n: int, contour: Contour) -> complex:
    def integrand(t: float) -> complex:
        return f(contour.path(t)) * contour.path_prime(t) / (contour.path(t) - z) ** (n + 1)

    return 1 / (2j * pi) * integrate(integrand, contour.start, contour.end)

# The function that we will take the derivative of
def f(z: complex) -> complex:
    return -sum(z ** n for n in range(1999)) / (z ** 2000 + z ** 1999 - 1)

# Unfortunately, this solving strategy doesn't work quite well for a couple reasons
# 1. If we choose a radius bigger than 1, everything blows up and overflows
# 2. If we choose a radius lesser than 1, everything goes to 0
# 3. A radius 1 probably isn't even correct because the function isn't analytic on the contour
# Maybe I should consider a different solution strategy. In the first place, this solution is
# way out there.
print(F_n(f, 0, 2000, CircleContour(1)))
