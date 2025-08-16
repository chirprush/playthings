import numpy as np

n = 4

best = 0
bestA = None

for b in range(3 ** (n * n)):
    A = np.zeros((n, n), dtype=np.int64)

    encoded = b

    for i in range(n * n):
        A[i % n, i // n] = [-1, 0, 1][encoded % 3]
        encoded //= 3

    d = np.linalg.det(A)

    if d > best:
        best = d
        bestA = A

        print(f"det: {best}")
        print(bestA)
