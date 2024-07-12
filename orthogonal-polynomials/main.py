from math import ceil
from sympy import Matrix, Rational

n = int(input("Enter a degree: "))

N = n // 2

# If my memory serves me right, this should generate polynomials orthogonal
# with respect to the inner product defined by integration over [-1, 1]

# I might derive some stuff again and write about it, perhaps instead using the inner product of integration over [0, 1] because that seems far easier.
def co(l, m):
    k = n % 2 + 2 * l
    i = (-k) % 2 + 2 * m
    return Rational(1, i + k + 1)

def res(l, m):
    k = n % 2 + 2 * l
    return Rational(-1, n + k + 1)

A = Matrix(N, N, co)
b = Matrix(N, 1, res)

print(A)
print(b)

coefficients = [*list(A.inv() * b), 1]

print(coefficients)

print(' + '.join(f"({c})x^{n % 2 + 2 * i}" for i, c in enumerate(coefficients)))
