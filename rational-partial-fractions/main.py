from math import prod, sin, cos, pi, e
from src.partial_frac import theta_k, r_k, a_k
from src.util import zround, zeq

if __name__ == "__main__":
    n = 4
    m = int(n / 2)

    k = 0

    print(zround(r_k(n, k)), zround(r_k(n, n - k - 1)))
    print(zround(r_k(n, k) + r_k(n, n - k - 1)))
    print(zround(2 * cos(theta_k(n, k))))
