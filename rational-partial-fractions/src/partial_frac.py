from math import prod, sin, cos, pi, e
from src.util import zround

# n is the degree of the polynomial in x^n + 1
# if n is odd, 2m + 1 = n
# if n is even, 2m = n
# \theta_k = \frac{(2k + 1) \pi}{n}
# r_k = exp(i \theta_k)

# Partial fractions for even n:
# \sum_{k = 0}^{m - 1} ( a_k x + b_k ) \prod_{j = 0, j \ne k}^{m - 1} (x^2 - 2\cos{\left( \theta_j \right)} x + 1) = 1
# a_k r_k + b_k = \prod{j = 0, j \ne k}^{m - 1} 1/(r_k^2 - 2\cos{\left( \theta_j \right)} r_k + 1) = A
# a_k r_{n-k-1} + b_k = \prod{j = 0, j \ne k}^{m - 1} 1/(r_{n-k-1}^2 - 2\cos{\left( \theta_j \right)} r_{n-k-1} + 1) = B
# a_k (r_k - r_{n-k-1}) = A - B
# a_k = (A - B)/(r_k - r_{n-k-1})
# ^ This is what I want to check

def theta_k(n, k):
    return (2 * k + 1) * pi / n

def r_k(n, k):
    return e ** (1j * theta_k(n, k))

# Each of these functions should be equal, and the only difference
# between them is that I've done some mathematical simplications. I'm
# doing this in order to check whether my math is actually correct.

# This specific function is literally the definition of what I'm
# doing, so it can't be wrong
def a_k_even0(n, k):
    m = int(n / 2)

    quad = lambda x, j: x ** 2 - 2 * cos(theta_k(n, j)) * x + 1

    A = prod(1 / quad(r_k(n, k), j) for j in range(m) if j != k)
    B = prod(1 / quad(r_k(n, n - k - 1), j) for j in range(m) if j != k)

    return (A - B) / (r_k(n, k) - r_k(n, n - k - 1))

# This function uses the limit simplification in place of the products
def a_k_even1(n, k):
    lim = lambda x: (2 * x - 2 * cos(theta_k(n, k))) / (n * x ** (n - 1))

    A = lim(r_k(n, k))
    B = lim(r_k(n, n - k - 1))

    return (A - B) / (r_k(n, k) - r_k(n, n - k - 1))

# This is a small simplification step that gets a common denominator
def a_k_even2(n, k):
    A = 1 / n * r_k(n, n - k - 1) ** (n - 1) * (2 * r_k(n, k) - 2 * cos(theta_k(n, k)))
    B = 1 / n * r_k(n, k) ** (n - 1) * (2 * r_k(n, n - k - 1) - 2 * cos(theta_k(n, k)))

    return (A - B) / (2j * sin(theta_k(n, k)))

# A small expanding of some of the terms and canceling out conjugates
def a_k_even3(n, k):
    r1 = r_k(n, k)
    r2 = r_k(n, n - k - 1)
    gamma = cos(theta_k(n, k))

    A = 2 / n * (r2 ** (n - 2) - gamma * r2 ** (n - 1) - r1 ** (n - 2) + gamma * r1 ** (n - 1))

    return A / (2j * sin(theta_k(n, k)))

# This is where the error comes in it seems
def a_k_even4(n, k):
    return 2 / n * (2j * sin((n - 1) * theta_k(n, k)) * cos(theta_k(n, k)) - 2j * sin((n - 2) * theta_k(n, k))) / (2j * sin(theta_k(n, k)))

def a_k_even5(n, k):
    return 4j / n * (sin(pi - theta_k(n, k)) * cos(theta_k(n, k)) - sin(2 * theta_k(n, k))) / (2j * sin(theta_k(n, k)))

def a_k_even6(n, k):
    return -2 / n * cos(theta_k(n, k))

def b_k_even0(n, k):
    a_k = a_k_even6(n, k)
    r1 = r_k(n, k)
    r2 = r_k(n, n - k - 1)
    gamma = 2 * cos(theta_k(n, k))

    A = (2 * r1 - gamma) / (n * r1 ** (n - 1))
    B = (2 * r2 - gamma) / (n * r2 ** (n - 1))

    return ((A + B) - a_k * (r1 + r2)) / 2

def b_k_even1(n, k):
    gamma = 2 * cos(theta_k(n, k))
    r1 = r_k(n, k)
    r2 = r_k(n, n - k - 1)

    return 1 / n * (2 * r2 ** (n - 2) - gamma * r2 ** (n - 1) + 2 * r1 ** (n - 2) - gamma * r1 ** (n - 1) + gamma ** 2) / 2

def b_k_even2(n, k):
    s = sin(theta_k(n, k))
    c = cos(theta_k(n, k))
    r1 = r_k(n, k)
    r2 = r_k(n, n - k - 1)

    return 1 / n * (r2 ** (n - 2) - c * r2 ** (n - 1) + r1 ** (n - 2) - c * r1 ** (n - 1) + 2 * c ** 2)

def b_k_even3(n, k):
    c = cos(theta_k(n, k))

    return 1 / n * (2 * cos(pi - 2 * theta_k(n, k)) - 2 * c * cos(pi - theta_k(n, k)) + 2 * c ** 2)

def b_k_even4(n, k):
    return 2 / n
