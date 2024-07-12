import numpy as np
from math import gcd

A = np.array([
    [1, 2, 3],
    [4, 5, 7],
    [1, 2, 10]
])

M = 13

det = round(np.linalg.det(A))

print("Determinant:", det)

if gcd(M, det) > 1:
    print("The order is indeterminate")
    exit(-1)

B = np.identity(A.shape[0])

k = 0

while k == 0 or not np.array_equal(B, np.identity(A.shape[0])):
    B = np.dot(A, B) % M
    k += 1

print(f"The order of A modulo {M} is {k}")
