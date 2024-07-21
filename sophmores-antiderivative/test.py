from util import feq, integrate, summate, SUM_INF
from math import factorial, log, exp, e

from playground import sophmore_integral, u_eu_rec_integral, u_eu_closed_sum

def test_exp_expansion() -> None:
    assert feq(
        sophmore_integral(0, 1),
        summate(
            lambda n: 1 / factorial(n) * integrate(lambda x: (x * log(x)) ** n, 0, 1),
            0,
            SUM_INF
        )
    )

def test_xln_integral_sub() -> None:
    for n in range(1, 20):
        assert feq(
            integrate(lambda x: (x * log(x)) ** n, 1, e),
            integrate(lambda x: x ** n * exp((n + 1) * x), 0, 1)
        )

def test_ueu_recursive() -> None:
    # Testing irrespective of previous integrals before
    for n in range(1, 20):
        for k in range(1, 20):
            assert feq(
                integrate(lambda x: x ** k * exp((n + 1) * x), 0, 1),
                u_eu_rec_integral(k, n, 0, 1)
            )

def test_ueu_closed_form() -> None:
    for n in range(1, 20):
        for k in range(1, 20):
            assert feq(
                integrate(lambda x: x ** k * exp((n + 1) * x), 1, 2),
                u_eu_closed_sum(k, n, 1, 2)
            )
