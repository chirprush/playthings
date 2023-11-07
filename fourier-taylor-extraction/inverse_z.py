from cmath import exp, pi
from math import prod

def X(n, q, z):
    return n / q + (1 - n / q) * z

def P(q, z):
    return prod(X(n, q, z) for n in range(1, 51))

def integrate(f, a, b, steps=100):
    dx = (b - a) / steps

    total = 0

    for i in range(steps):
        y1 = f(a + i * dx)
        y2 = f(a + (i + 1) * dx)

        total += 0.5 * (y1 + y2) * dx

    return total

def p20(q):
    return (integrate(lambda t: P(q, exp(1j * t)) * exp(-20j * t), 0, 2 * pi, 1000) / (2 * pi)).real

left = 52
right = 53
guess = 52.5

target = 2 / 100

for _ in range(50):
    current = p20(guess)

    if current < target:
        right = guess
    elif current > target:
        left = guess

    guess = (left + right) / 2

print(guess, p20(guess))
