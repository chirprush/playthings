from util import integrate, summate, SUM_INF
from math import exp, log, factorial

def sophmore_integral(a: float, b: float) -> float:
    return integrate(lambda x: x ** x, a, b)

def u_eu_rec_integral(k: int, n: int, a: float, b: float) -> float:
    if k == 0:
        return integrate(lambda x: exp((n + 1) * x), a, b)
    vw = lambda x: 1 / (n + 1) * x ** k * exp((n + 1) * x)
    return (vw(b) - vw(a)) - k / (n + 1) * u_eu_rec_integral(k - 1, n, a, b)

def u_eu_closed_sum(k: int, n: int, a: float, b: float) -> float:
    antiderivative = lambda x: summate(
        lambda j: (-1) ** j / (n + 1) ** (j + 1) * factorial(k) / factorial(k - j) * x ** (n + 1) * log(x) ** (k - j),
        0,
        k
    )

    return antiderivative(b) - antiderivative(a)
