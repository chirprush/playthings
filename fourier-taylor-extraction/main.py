# https://artofproblemsolving.com/wiki/index.php/2022_AIME_II_Problems/Problem_13
# 2022 AIME II Problem 13 using Fourier analysis
# ...and, well, a calculator

from cmath import exp, pi
from math import prod

def P(x):
    return (x ** 2310 - 1) ** 6 / ((x ** 105 - 1) * (x ** 70 - 1) * (x ** 42 - 1) * (x ** 30 - 1))
    # return prod((1 - x ** k) ** (-1) for k in [1, 2, 5, 10, 20, 50, 100, 200])

def PExp(t):
    return P(C * exp(1j * t))

def integrate(f, a, b, steps=100):
    dx = (b - a) / steps

    total = 0

    for i in range(steps):
        y1 = f(a + i * dx)
        y2 = f(a + (i + 1) * dx)

        total += 0.5 * (y1 + y2) * dx

    return total

# Depending on the function and N, the values of C that work are a bit finnicky
C = 0.999999
N = 2022

print(integrate(lambda t: PExp(t) * exp(-N * 1j * t), 0, 2 * pi, 100000) * C ** (-N) / (2 * pi))
