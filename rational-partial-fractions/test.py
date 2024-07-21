from math import sqrt
from src.util import zeq
from src.partial_frac import a_k_even0, a_k_even1, a_k_even2, a_k_even3, a_k_even4, a_k_even5, a_k_even6
from src.partial_frac import b_k_even0, b_k_even1, b_k_even2, b_k_even3, b_k_even4

a_k_funcs = [a_k_even0, a_k_even1, a_k_even2, a_k_even3, a_k_even4, a_k_even5, a_k_even6]
b_k_funcs = [b_k_even0, b_k_even1, b_k_even2, b_k_even3, b_k_even4]

def test_n_even_a_k():
    a_k_coefficients = [
        [0],
        [-1 / (2 * sqrt(2)), 1 / (2 * sqrt(2))],
        [-1 / (2 * sqrt(3)), 0, 1 / (2 * sqrt(3))]
    ]

    for m in range(1, len(a_k_coefficients) + 1):
        n = 2 * m

        for a_k in a_k_funcs:
            for k in range(m):
                assert zeq(a_k(n, k), a_k_coefficients[m - 1][k])

def test_n_even_b_k():
    b_k_coefficients = [
        [1],
        [1 / 2, 1 / 2],
        [1 / 3, 1 / 3, 1 / 3]
    ]

    for m in range(1, len(b_k_coefficients) + 1):
        n = 2 * m

        for b_k in b_k_funcs:
            for k in range(m):
                assert zeq(b_k(n, k), b_k_coefficients[m - 1][k])
