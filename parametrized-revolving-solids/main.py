from cmath import sqrt
from math import cos, sin, tan, pi

g = 9.81

def integrate(f, a, b, steps=100):
    dx = (b - a) / steps

    total = 0

    for i in range(steps):
        y1 = f(a + i * dx)
        y2 = f(a + (i + 1) * dx)

        total += 0.5 * (y1 + y2) * dx

    return total

def basically_zero(t):
    return abs(t) < 1e-6

def h(y, theta):
    return 400 * cos(theta) ** 2 / g * (tan(theta) + sqrt(tan(theta) ** 2 + (2 * g * (100-y))/(400 * cos(theta) ** 2)))

def radius(y):
    # Quite a primitive way to do it but hey hey
    greatest = 0

    steps = 500
    interval = pi / 2
    dtheta = interval / steps

    for i in range(steps + 1):
        x = h(y, dtheta * i)

        if basically_zero(x.imag) and x.real > greatest:
            greatest = x.real

    return greatest

# This does not work :(
print(pi * integrate(lambda y: radius(y) ** 2, 0, 120, 3001))
